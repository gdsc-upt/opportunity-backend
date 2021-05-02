from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import RefreshToken

from administration.models import User
from .serializers import (
    LoginSerializer,
    JWTSerializerWithExpiration,
    JWTSerializer,
    UserDetailsSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    PasswordChangeSerializer,
)
from .utils import jwt_encode

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        "password", "old_password", "new_password1", "new_password2"
    )
)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    throttle_scope = "auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    @staticmethod
    def get_response_serializer():
        if getattr(settings, "JWT_AUTH_RETURN_EXPIRATION", False):
            response_serializer = JWTSerializerWithExpiration
        else:
            response_serializer = JWTSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data["user"]
        self.access_token, self.refresh_token = jwt_encode(self.user)
        django_login(self.request, self.user)

    def get_response(self):
        serializer_class = self.get_response_serializer()

        return_expiration_times = getattr(settings, "JWT_AUTH_RETURN_EXPIRATION", False)
        data = {
            "user": self.user,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
        }
        if return_expiration_times:
            access_token_expiration = (
                    timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME
            )
            refresh_token_expiration = (
                    timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME
            )
            data["access_token_expiration"] = access_token_expiration
            data["refresh_token_expiration"] = refresh_token_expiration

        serializer = serializer_class(
            instance=data, context=self.get_serializer_context()
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class LogoutView(APIView):
    throttle_scope = "auth"

    def post(self, request, *args, **kwargs):
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)

        response = Response(
            {"detail": _("Successfully logged out.")}, status=status.HTTP_200_OK
        )

        if "rest_framework_simplejwt.token_blacklist" in settings.INSTALLED_APPS:
            # add refresh token to blacklist
            try:
                token = RefreshToken(request.data["refresh"])
                token.blacklist()
            except KeyError:
                response.data = {
                    "detail": _("Refresh token was not included in request data.")
                }
                response.status_code = status.HTTP_401_UNAUTHORIZED
            except (TokenError, AttributeError, TypeError) as error:
                if hasattr(error, "args"):
                    if (
                            "Token is blacklisted" in error.args
                            or "Token is invalid or expired" in error.args
                    ):
                        response.data = {"detail": _(error.args[0])}
                        response.status_code = status.HTTP_401_UNAUTHORIZED
                    else:
                        response.data = {"detail": _("An error has occurred.")}
                        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                else:
                    response.data = {"detail": _("An error has occurred.")}
                    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.none()


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "auth"

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("Password has been reset with the new password.")})


class PasswordChangeView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)
    throttle_scope = "auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved.")})

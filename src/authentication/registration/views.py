from .serializers import (
    VerifyEmailSerializer,
    RegisterSerializer,
)
from django.http import Http404
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.registration.models import EmailConfirmationHMAC

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("password1", "password2")
)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    throttle_scope = "auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(self.request)
        return Response(
            {"detail": _("Verification e-mail sent.")},
            status=status.HTTP_201_CREATED,
        )


class VerifyEmailView(GenericAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ("POST", "OPTIONS", "HEAD")

    def get_object(self) -> EmailConfirmationHMAC:
        key = self.kwargs["key"]
        if emailconfirmation := EmailConfirmationHMAC.from_key(key):
            return emailconfirmation
        raise Http404()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs["key"] = serializer.validated_data["key"]
        confirmation = self.get_object()
        confirmation.confirm()
        return Response(
            {"detail": _("email successfully verified!")}, status=status.HTTP_200_OK
        )

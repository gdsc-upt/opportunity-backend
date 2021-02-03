import json
from typing import AnyStr

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from requests.exceptions import HTTPError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from administration.models import User
from authentication.registration.models import EmailConfirmationHMAC

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.helpers import complete_social_login
    from allauth.socialaccount.models import SocialAccount
    from allauth.socialaccount.providers.base import AuthProcess
    from allauth.utils import email_address_exists, get_username_max_length
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")


class SocialAccountSerializer(serializers.ModelSerializer):
    """
    serialize allauth SocialAccounts for use with a REST API
    """

    class Meta:
        model = SocialAccount
        fields = (
            "id",
            "provider",
            "uid",
            "last_login",
            "date_joined",
        )


class SocialLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=False, allow_blank=True)
    code = serializers.CharField(required=False, allow_blank=True)
    id_token = serializers.CharField(required=False, allow_blank=True)

    def _get_request(self):
        request = self.context.get("request")
        if not isinstance(request, HttpRequest):
            request = request._request
        return request

    def get_social_login(self, adapter, app, token, response):
        """
        :param adapter: allauth.socialaccount Adapter subclass.
            Usually OAuthAdapter or Auth2Adapter
        :param app: `allauth.socialaccount.SocialApp` instance
        :param token: `allauth.socialaccount.SocialToken` instance
        :param response: Provider's response for OAuth1. Not used in the
        :returns: A populated instance of the
            `allauth.socialaccount.SocialLoginView` instance
        """
        request = self._get_request()
        social_login = adapter.complete_login(request, app, token, response=response)
        social_login.token = token
        return social_login

    def validate(self, attrs):
        view = self.context.get("view")
        request = self._get_request()

        if not view:
            raise serializers.ValidationError(
                _("View is not defined, pass it as a context variable")
            )

        adapter_class = getattr(view, "adapter_class", None)
        if not adapter_class:
            raise ValidationError(_("Define adapter_class in view"))

        adapter = adapter_class(request)
        app = adapter.get_provider().get_app(request)

        # More info on code vs access_token
        # http://stackoverflow.com/questions/8666316/facebook-oauth-2-0-code-and-token

        access_token = attrs.get("access_token")
        code = attrs.get("code")
        # Case 1: We received the access_token
        if access_token:
            tokens_to_parse = {"access_token": access_token}
            # For sign in with apple
            id_token = attrs.get("id_token")
            if id_token:
                tokens_to_parse["id_token"] = id_token

        # Case 2: We received the authorization code
        elif code:
            self.callback_url = getattr(view, "callback_url", None)
            self.client_class = getattr(view, "client_class", None)

            if not self.callback_url:
                raise serializers.ValidationError(_("Define callback_url in view"))
            if not self.client_class:
                raise serializers.ValidationError(_("Define client_class in view"))

            provider = adapter.get_provider()
            scope = provider.get_scope(request)
            client = self.client_class(
                request,
                app.client_id,
                app.secret,
                adapter.access_token_method,
                adapter.access_token_url,
                self.callback_url,
                scope,
                scope_delimiter=adapter.scope_delimiter,
                headers=adapter.headers,
                basic_auth=adapter.basic_auth,
            )
            token = client.get_access_token(code)
            access_token = token["access_token"]
            tokens_to_parse = {"access_token": access_token}

            # If available we add additional data to the dictionary
            for key in ["refresh_token", "id_token", adapter.expires_in_key]:
                if key in token:
                    tokens_to_parse[key] = token[key]
        else:
            raise serializers.ValidationError(
                _("Incorrect input. access_token or code is required.")
            )

        social_token = adapter.parse_token(tokens_to_parse)
        social_token.app = app

        try:
            login = self.get_social_login(adapter, app, social_token, access_token)
            complete_social_login(request, login)
        except HTTPError:
            raise serializers.ValidationError(_("Incorrect value"))

        if not login.is_existing:
            # We have an account already signed up in a different flow
            # with the same email address: raise an exception.
            # This needs to be handled in the frontend. We can not just
            # link up the accounts due to security constraints
            if allauth_settings.UNIQUE_EMAIL:
                # Do we have an account already with this email address?
                account_exists = (
                    get_user_model()
                    .objects.filter(
                        email=login.user.email,
                    )
                    .exists()
                )
                if account_exists:
                    raise serializers.ValidationError(
                        _("User is already registered with this e-mail address.")
                    )

            login.lookup()
            login.save(request, connect=True)

        attrs["user"] = login.account.user

        return attrs


class SocialConnectMixin(object):
    def get_social_login(self, *args, **kwargs):
        """
        Set the social login process state to connect rather than login
        Refer to the implementation of get_social_login in base class and to the
        allauth.socialaccount.helpers module complete_social_login function.
        """
        social_login = super(SocialConnectMixin, self).get_social_login(*args, **kwargs)
        social_login.state["process"] = AuthProcess.CONNECT
        return social_login


class SocialConnectSerializer(SocialConnectMixin, SocialLoginSerializer):
    pass


def email_exists(email: AnyStr):
    return User.objects.filter(email__iexact=email).exists()


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise ValidationError(_("The two password fields didn't match."))
        if data["email"] and email_exists(data["email"]):
            raise ValidationError(
                _("A user is already registered with this e-mail address.")
            )
        password = data["password1"]
        password_min_length = 8
        if password_min_length and len(password) < password_min_length:
            raise ValidationError(
                _(f"Password must be a minimum of {password_min_length} characters.")
            )
        validate_password(password)
        return data

    def get_cleaned_data(self):
        return {
            "password": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def save(self, request):
        user = User()
        user = self.save_user(user, self.get_cleaned_data())
        email_confirmation = EmailConfirmationHMAC(user)
        email_confirmation.send(request)
        return user

    def save_user(self, user, data):
        print(json.dumps(data, indent=4))
        first_name = data.get("first_name")
        if not first_name:
            raise ValidationError(_("first_name is required!"))
        last_name = data.get("last_name")
        email = data.get("email")
        self.user_field(user, "email", email)
        self.user_field(user, "first_name", first_name)
        self.user_field(user, "last_name", last_name)
        user.set_password(data["password"])
        user.username = str(user.email).split("@", 1)[0]  # getting username from email
        user.is_email_confirmed = False
        user.save()
        return user

    @staticmethod
    def user_field(user: User, field: AnyStr, value):
        field_meta = User._meta.get_field(field)
        max_length = field_meta.max_length
        value = value[0:max_length]
        setattr(user, field, value)


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()

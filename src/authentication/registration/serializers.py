from typing import AnyStr

from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer

from administration.models import User
from authentication.registration.models import EmailConfirmationHMAC


def email_exists(email: AnyStr):
    return User.objects.filter(email__iexact=email).exists()


class RegisterSerializer(Serializer):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password1 = CharField()
    password2 = CharField()

    def validate(self, data):
        errors = []
        if not data["first_name"]:
            errors.append(ValidationError(_("first_name is required!")))
        if data["password1"] != data["password2"]:
            errors.append(ValidationError(_("The two password fields didn't match.")))
        if data["email"] and email_exists(data["email"]):
            errors.append(
                ValidationError(
                    _("A user is already registered with this e-mail address.")
                )
            )
        password = data["password1"]
        password_min_length = 8
        if password_min_length and len(password) < password_min_length:
            errors.append(
                ValidationError(
                    _(
                        f"Password must be a minimum of {password_min_length} characters."
                    )
                )
            )
        try:
            validate_password(password)
        except ValidationError as exc:
            errors.append(exc)
        if errors:
            raise ValidationError(errors)
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
        first_name = data.get("first_name")
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


class VerifyEmailSerializer(Serializer):
    key = serializers.CharField()

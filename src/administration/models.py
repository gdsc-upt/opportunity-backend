from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = EmailField(_('email address'), unique=True)

    class Meta:
        db_table = 'auth_user'

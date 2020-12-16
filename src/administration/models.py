from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, Model
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = EmailField(_('email address'), unique=True)

    class Meta:
        db_table = 'auth_user'


class ExampleModel(Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField(null=True)
    age = models.IntegerField()


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    link = models.URLField()
    image = models.ImageField(blank=True, default=None)
    parent = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.name

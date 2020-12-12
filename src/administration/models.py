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

class Partner(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    website = models.URLField(blank=True, default= None)
    logo = models.ImageField(blank=True, default=None)
    isPublished

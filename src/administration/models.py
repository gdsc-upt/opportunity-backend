from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, Model, DateTimeField, BooleanField, ImageField, URLField, SlugField, CharField
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = EmailField(_('email address'), unique=True)

    class Meta:
        db_table = 'auth_user'


class ExampleModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField(null=True)
    age = models.IntegerField()


class Partner(Model):
    name = CharField(max_length=100)
    slug = SlugField()
    website = URLField(blank=True, default=None)
    logo = ImageField(blank=True, default=None)
    is_published = BooleanField()
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=1000)
    is_published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

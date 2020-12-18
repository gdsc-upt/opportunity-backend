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


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=1000)
    is_published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

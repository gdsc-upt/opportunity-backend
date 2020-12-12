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


class Organization(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)
    #   representant = models.ForeignKey(blank=True, on_delete=models.CASCADE)
    website = models.URLField(blank=True, default=None)
    description = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=40, blank=True)
    # opportunities = models.ForeignKey(blank=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    bla = models.CharField(max_length=21, blank=True)

    def __str__(self):
        return self.name

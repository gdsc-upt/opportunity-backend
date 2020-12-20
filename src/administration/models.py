from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, Model, DateTimeField, BooleanField, ImageField, URLField, SlugField, CharField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
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


class Organisation(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)
    website = models.URLField(blank=True, default=None)
    description = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=40, blank=True)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    url = models.URLField(blank=True, default=None)
    description = models.TextField(max_length=300)
    deadline = models.DateTimeField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "opportunity"
        verbose_name_plural = "opportunities"


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    link = models.URLField()
    image = models.ImageField(blank=True, default=None)
    parent = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(blank=True, default=None)
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    email = models.CharField(max_length=50)
    slug = models.SlugField()
    # opportunity_categories = models.ManyToManyField(OpportunityCategory)
    other = models.CharField(max_length=500)
    is_published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

class WantToHelp(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField (max_length=255)
    description=models.TextField()


class OpportunityCategory(models.Model):
    name=models.CharField(max_length=225)
    slug=models.SlugField()
    opportunities=models.ManyToManyField(Opportunity)
    created=models.DateTimeField()
    updated=models.DateTimeField()



from django.db.models import CharField, URLField, ImageField, TextField, Model, EmailField, ManyToManyField
from django.utils.translation import gettext_lazy as _

from administration.models import Category
from common.models import SlugableModel, PublishableModel, CreatedUpdatedModel


class Newsletter(CreatedUpdatedModel):
    email = EmailField(max_length=250, unique=True)
    categories = ManyToManyField(Category, blank=True)
    other = CharField(max_length=500, blank=True, help_text='Other categories that are not listed above')

    class Meta:
        db_table = 'newsletters'

    def __str__(self):
        return self.email


class Partner(SlugableModel, PublishableModel, CreatedUpdatedModel):
    name = CharField(max_length=100)
    website = URLField(blank=True, default=None)
    logo = ImageField(blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'partners'


class Faq(PublishableModel, CreatedUpdatedModel):
    question = CharField(max_length=300)
    answer = TextField(max_length=1000)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'faqs'


class MenuItem(Model):
    name = CharField(max_length=30)
    link = URLField()
    image = ImageField(blank=True, default=None)
    parent = CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu_items'


class Article(SlugableModel, PublishableModel, CreatedUpdatedModel):
    name = CharField(max_length=100)
    image = ImageField(blank=True, default=None)
    description = CharField(max_length=2000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'articles'


class WantToHelp(Model):
    name = CharField(max_length=225)
    email = EmailField(max_length=255)
    description = TextField()

    class Meta:
        db_table = 'want_to_help'
        verbose_name = _('want to help')
        verbose_name_plural = _('want to help')


class Contact(CreatedUpdatedModel):
    name = CharField(max_length=200)
    email = EmailField(max_length=200)
    subject = CharField(max_length=300)
    message = TextField(max_length=2000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contacts'

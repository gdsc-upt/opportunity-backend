from django.db.models import CharField, URLField, ImageField, TextField, Model, EmailField, ManyToManyField

from administration.models import OpportunityCategory
from common.models import SlugableModel, PublishableModel, CreatedUpdatedModel


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


class Newsletter(CreatedUpdatedModel):
    email = EmailField(max_length=50)
    opportunity_categories = ManyToManyField(OpportunityCategory)
    other = CharField(max_length=500)

    class Meta:
        db_table = 'newsletters'

    def __str__(self):
        return self.email

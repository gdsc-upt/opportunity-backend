from django.db.models import CharField, URLField, ImageField, TextField, Model, EmailField, ManyToManyField, ForeignKey, \
    SET_NULL, \
    PositiveIntegerField, Q
from django.utils.translation import gettext_lazy as _

from administration.models import Category
from common.models import SlugableModel, PublishableModel, CreatedUpdatedModel


class Newsletter(CreatedUpdatedModel):
    email = EmailField(max_length=250, unique=True)
    categories = ManyToManyField(Category, blank=True)
    other = CharField(max_length=500, blank=True, help_text=_('Other categories that are not listed above'))

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
    TYPES = (
        ('ExternalLink', _('Link outside our domain (ex: google.com/milk)')),
        ('InternalLink', _('Link inside our domain (ex: /contact)'))
    )

    name = CharField(max_length=200)
    link = CharField(max_length=1000)
    type = CharField(max_length=20, choices=TYPES, default='InternalLink')
    parent = ForeignKey('MenuItem', on_delete=SET_NULL, blank=True, null=True, related_name='children')
    order_index = PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    def __str__(self):
        return self.name

    # https://medium.com/@tnesztler/recursive-queries-as-querysets-for-parent-child-relationships-self-manytomany-in-django-671696dfe47
    def get_children(self, include_self=True):
        return MenuItem.objects.filter(self.get_children_filter(include_self))

    def get_children_filter(self, include_self=True):
        filters = Q(pk=0)
        if include_self:
            filters |= Q(pk=self.pk)
        for item in MenuItem.objects.filter(parent=self):
            if children_filter := item.get_children_filter(include_self=True):
                filters |= children_filter
        return filters

    class Meta:
        db_table = 'menu_items'
        ordering = ['order_index']


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


class Setting(SlugableModel, CreatedUpdatedModel):
    TYPES = (
        ("TEXT", "Text"),
        ("IMAGE", "Image")
    )

    description = TextField(max_length=250, blank=True, default='')
    type = CharField(max_length=5, choices=TYPES, default='TEXT')
    value = TextField(max_length=300, blank=True, default='')
    image = ImageField(blank=True, default=None)

    class Meta:
        db_table = 'settings'

    def str(self):
        return self.slug.replace('_', ' ').capitalize()

from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, Model, DateTimeField, URLField, CharField, SET_NULL, TextField, \
    ForeignKey, CASCADE, ManyToManyField, OneToOneField
from django.utils.translation import gettext_lazy as _

from common.models import SlugableModel, PublishableModel, CreatedUpdatedModel


class Organisation(SlugableModel, PublishableModel, CreatedUpdatedModel):
    name = CharField(max_length=20)
    website = URLField(blank=True, default=None)
    description = TextField(max_length=300, blank=True)
    location = CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'organisations'


class User(AbstractUser):
    email = EmailField(_('email address'), unique=True)

    class Meta:
        db_table = 'auth_user'


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    organisation = ForeignKey(Organisation, on_delete=SET_NULL, null=True)
    description = TextField(max_length=300)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'user_profiles'


class Opportunity(SlugableModel, CreatedUpdatedModel):
    name = CharField(max_length=50)
    url = URLField(blank=True, default=None)
    description = TextField(max_length=300)
    deadline = DateTimeField()
    organisation = ForeignKey(Organisation, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'opportunities'
        verbose_name = _("opportunity")
        verbose_name_plural = _("opportunities")


class OpportunityCategory(SlugableModel, CreatedUpdatedModel):
    name = CharField(max_length=225)
    opportunities = ManyToManyField(Opportunity)

    class Meta:
        db_table = 'opportunity_categories'
        verbose_name = _('opportunity category')
        verbose_name_plural = _('opportunity categories')


class WantToHelp(Model):
    name = CharField(max_length=225)
    email = EmailField(max_length=255)
    description = TextField()

    class Meta:
        db_table = 'want_to_help'
        verbose_name = _('want to help')
        verbose_name_plural = _('want to help')

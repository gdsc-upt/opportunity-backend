from django.contrib.auth.models import AbstractUser

from django.db.models import (
    EmailField,
    DateTimeField,
    URLField,
    CharField,
    SET_NULL,
    TextField,
    ForeignKey,
    CASCADE,
    ManyToManyField,
    OneToOneField,
    BooleanField,
)
from django.utils.translation import gettext_lazy as _

from common.models import SlugableModel, PublishableModel, BaseModel


class Organisation(SlugableModel, PublishableModel, BaseModel):
    name = CharField(_("name"), max_length=20)
    website = URLField(_("website"), blank=True, default=None)
    description = TextField(_("description"), max_length=300, blank=True)
    location = CharField(_("location"), max_length=40, blank=True)

    def get_absolute_url(self):
        return f"/organisations/{self.slug}"

    class Meta:
        db_table = "organisations"


class User(AbstractUser):
    email = EmailField(_("email address"), unique=True)
    is_email_confirmed = BooleanField(_("email confirmed"), default=False)

    class Meta:
        db_table = "auth_user"


class UserProfile(BaseModel):
    user = OneToOneField(
        User,
        verbose_name=_("user"),
        on_delete=CASCADE,
        related_name="profile",
        related_query_name="profile",
    )
    organisation = ForeignKey(
        Organisation,
        verbose_name=_("organisation"),
        on_delete=SET_NULL,
        null=True,
        related_name="profiles",
        related_query_name="profile",
    )
    description = TextField(_("description"), max_length=300)

    class Meta:
        db_table = "user_profiles"


class Opportunity(PublishableModel, SlugableModel, BaseModel):
    name = CharField(_("name"), max_length=50)
    url = URLField(_("url"), blank=True, default=None)
    description = TextField(_("description"), max_length=300)
    deadline = DateTimeField(_("deadline"))
    organisation = ForeignKey(
        Organisation,
        verbose_name=_("organisation"),
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="opportunities",
        related_query_name="opportunity",
    )

    class Meta:
        db_table = "opportunities"
        verbose_name = _("opportunity")
        verbose_name_plural = _("opportunities")


class Category(SlugableModel, BaseModel):
    name = CharField(_("name"), max_length=225)
    opportunities = ManyToManyField(
        Opportunity,
        verbose_name=_("opportunities"),
        blank=True,
        related_name="categories",
        related_query_name="category",
    )

    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

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
)
from django.utils.translation import gettext_lazy as _

from common.models import SlugableModel, PublishableModel, BaseModel


class Organisation(SlugableModel, PublishableModel, BaseModel):
    name = CharField(max_length=20)
    website = URLField(blank=True, default=None)
    description = TextField(max_length=300, blank=True)
    location = CharField(max_length=40, blank=True)

    def get_absolute_url(self):
        return f"/organisations/{self.slug}"

    class Meta:
        db_table = "organisations"


class User(AbstractUser):
    email = EmailField(_("email address"), unique=True)

    class Meta:
        db_table = "auth_user"


class UserProfile(BaseModel):
    user = OneToOneField(
        User, on_delete=CASCADE, related_name="profile", related_query_name="profile"
    )
    organisation = ForeignKey(
        Organisation,
        on_delete=SET_NULL,
        null=True,
        related_name="profiles",
        related_query_name="profile",
    )
    description = TextField(max_length=300)

    class Meta:
        db_table = "user_profiles"


class Opportunity(PublishableModel, SlugableModel, BaseModel):
    name = CharField(max_length=50)
    url = URLField(blank=True, default=None)
    description = TextField(max_length=300)
    deadline = DateTimeField()
    organisation = ForeignKey(
        Organisation,
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
    name = CharField(max_length=225)
    opportunities = ManyToManyField(
        Opportunity, blank=True, related_name="categories", related_query_name="category"
    )

    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

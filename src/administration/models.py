from django.contrib.auth.models import AbstractUser
from django.db.models import (
    EmailField,
    Model,
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
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from common.models import SlugableModel, PublishableModel, CreatedUpdatedModel


class Organisation(SlugableModel, PublishableModel, CreatedUpdatedModel):
    name = CharField(max_length=20)
    website = URLField(blank=True, default=None)
    description = TextField(max_length=300, blank=True)
    location = CharField(max_length=40, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f"/organisations/{self.slug}"

    def get_obj_url(self):
        from django.urls import reverse

        url = reverse(
            f"admin:{self._meta.app_label}_{self._meta.model_name}_change", args=[str(self.id)]
        )
        return format_html(f"<a href='{url}'>{self.name}</a>")

    class Meta:
        db_table = "organisations"


class User(AbstractUser):
    email = EmailField(_("email address"), unique=True)

    class Meta:
        db_table = "auth_user"


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    organisation = ForeignKey(Organisation, on_delete=SET_NULL, null=True)
    description = TextField(max_length=300)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "user_profiles"


class Opportunity(PublishableModel, SlugableModel, CreatedUpdatedModel):
    name = CharField(max_length=50)
    url = URLField(blank=True, default=None)
    description = TextField(max_length=300)
    deadline = DateTimeField()
    organisation = ForeignKey(Organisation, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "opportunities"
        verbose_name = _("opportunity")
        verbose_name_plural = _("opportunities")


class Category(SlugableModel, CreatedUpdatedModel):
    name = CharField(max_length=225)
    opportunities = ManyToManyField(Opportunity, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

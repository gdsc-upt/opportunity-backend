from django.db.models import (
    CharField,
    URLField,
    ImageField,
    TextField,
    Model,
    EmailField,
    ManyToManyField,
    ForeignKey,
    SET_NULL,
    PositiveIntegerField,
    Q,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _
from django.db.models.constraints import CheckConstraint

from administration.models import Category
from common.models import SlugableModel, PublishableModel, BaseModel

from common.utils import get_upload_path


class Newsletter(BaseModel):
    email = EmailField(_("email"), max_length=250, unique=True)
    categories = ManyToManyField(
        Category,
        verbose_name=_("categories"),
        blank=True,
        related_name="newsletters",
        related_query_name="newsletter",
    )
    other = CharField(
        max_length=500,
        verbose_name=_("other"),
        blank=True,
        help_text=_("Other categories that are not listed above"),
    )

    class Meta:
        db_table = "newsletters"


class Partner(SlugableModel, PublishableModel, BaseModel):
    name = CharField(_("name"), max_length=100)
    website = URLField(_("website"), blank=True, default=None)
    logo = ImageField(_("logo"), blank=True, default=None, upload_to=get_upload_path)

    class Meta:
        db_table = "partners"


class Faq(PublishableModel, BaseModel):
    question = CharField(_("question"), max_length=300)
    answer = TextField(_("answer"), max_length=1000)

    def __str__(self):
        return str(self.question)

    class Meta:
        db_table = "faqs"


class MenuTypes(TextChoices):
    EXTERNAL_LINK = "ExternalLink", _("Link outside our domain (ex: google.com/milk)")
    INTERNAL_LINK = "InternalLink", _("Link inside our domain (ex: /contact)")


class MenuItem(BaseModel):
    name = CharField(_("name"), max_length=200)
    link = CharField(_("link"), max_length=1000)
    type = CharField(
        _("type"),
        max_length=20,
        choices=MenuTypes.choices,
        default=MenuTypes.INTERNAL_LINK,
    )
    parent = ForeignKey(
        "MenuItem",
        verbose_name=_("parent"),
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name="children",
    )
    order_index = PositiveIntegerField(
        _("order"), default=0, blank=False, db_index=True
    )

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
        db_table = "menu_items"
        ordering = ["order_index"]
        constraints = [
            CheckConstraint(
                name="menuitem_type_valid", check=Q(type__in=MenuTypes.values)
            )
        ]


class Article(SlugableModel, PublishableModel, BaseModel):
    name = CharField(_("name"), max_length=100)
    image = ImageField(_("image"), blank=True, default=None, upload_to=get_upload_path)
    description = CharField(_("description"), max_length=2000)

    class Meta:
        db_table = "articles"


class WantToHelp(Model):
    name = CharField(_("name"), max_length=225)
    email = EmailField(_("email"), max_length=255)
    description = TextField(_("description"))

    class Meta:
        db_table = "want_to_help"
        verbose_name = _("want to help")
        verbose_name_plural = _("want to help")


class Contact(BaseModel):
    name = CharField(_("name"), max_length=200)
    email = EmailField(_("email"), max_length=200)
    subject = CharField(_("subject"), max_length=300)
    message = TextField(_("message"), max_length=2000)

    class Meta:
        db_table = "contacts"


class SettingTypes(TextChoices):
    TEXT = "TEXT", _("Text")
    IMAGE = "IMAGE", _("Image")


class Setting(SlugableModel, BaseModel):
    type = CharField(
        _("type"), max_length=5, choices=SettingTypes.choices, default=SettingTypes.TEXT
    )
    value = TextField(_("value"), max_length=300, default="")
    image = ImageField(_("image"), blank=True, default=None, upload_to=get_upload_path)
    description = TextField(_("description"), max_length=250, blank=True, default="")

    class Meta:
        db_table = "settings"
        constraints = [
            CheckConstraint(
                name="setting_type_valid", check=(Q(type__in=SettingTypes.values))
            )
        ]

    def __str__(self):
        return self.slug.replace("_", " ").capitalize()

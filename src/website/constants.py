from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class MenuTypes(TextChoices):
    EXTERNAL_LINK = "ExternalLink", _("Link outside our domain (ex: google.com/milk)")
    INTERNAL_LINK = "InternalLink", _("Link inside our domain (ex: /contact)")


class SettingTypes(TextChoices):
    TEXT = "TEXT", _("Text")
    IMAGE = "IMAGE", _("Image")

from typing import Optional

from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from administration.models import User, Organisation, Opportunity, Category, UserProfile
from common.admin import BaseModelAdmin, SlugableModelAdmin, CREATED_MODIFIED
from common.admin_site import admin_site


@register(User, site=admin_site)
class UserAdmin(BaseUserAdmin):
    search_fields = ("username", "email", "first_name", "last_name")


@register(UserProfile, site=admin_site)
class UserProfileAdmin(ModelAdmin):
    list_display = ("user", "organisation", "description")
    list_filter = ("organisation",)
    search_fields = ("user", "organization")
    autocomplete_fields = ("user", "organisation")


@register(Group, site=admin_site)
class CustomGroupAdmin(GroupAdmin):
    pass


@register(Organisation, site=admin_site)
class OrganisationAdmin(BaseModelAdmin, SlugableModelAdmin):
    search_fields = ("name",)


@register(Opportunity, site=admin_site)
class OpportunityAdmin(BaseModelAdmin, SlugableModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "url",
                    "organisation",
                    "description",
                    "deadline",
                    "is_published",
                )
            },
        ),
        CREATED_MODIFIED,
    )
    list_display = (
        "name",
        "show_org_url",
        "deadline",
        "show_opp_url",
        "description",
        "is_published",
    )
    list_filter = ("deadline", "organisation")
    list_editable = ("is_published",)
    list_select_related = ("organisation",)
    autocomplete_fields = ("organisation",)
    search_fields = ("name",)

    @staticmethod
    def show_opp_url(obj: Opportunity):
        return format_html(f"<a href='{obj.url}'>{obj.url}</a>")

    show_opp_url.short_description = "url"

    @staticmethod
    def show_org_url(obj: Opportunity) -> Optional:
        if obj.organisation:
            return obj.organisation.href
        return None

    show_org_url.short_description = "organisation"


@register(Category, site=admin_site)
class CategoryAdmin(BaseModelAdmin, SlugableModelAdmin):
    fieldsets = ((None, {"fields": ("name", "slug", "opportunities")}), CREATED_MODIFIED)
    filter_horizontal = ("opportunities",)
    list_display = ("name", "slug", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("name",)

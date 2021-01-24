from typing import Optional

from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from administration.models import User, Organisation, Opportunity, Category, UserProfile
from common.admin import BaseModelAdmin, SlugableModelAdmin, CREATED_UPDATED
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
        CREATED_UPDATED,
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
    autocomplete_fields = ("organisation",)
    search_fields = ("name",)

    @staticmethod
    def show_opp_url(obj):
        return format_html(f"<a href='{obj.url}'>{obj.url}</a>")

    show_opp_url.short_description = "url"

    @staticmethod
    def show_org_url(obj: Opportunity) -> Optional:
        if obj.organisation:
            return obj.organisation.get_obj_url()
        return None

    show_org_url.short_description = "organisation"


@register(Category, site=admin_site)
class CategoryAdmin(BaseModelAdmin, SlugableModelAdmin):
    fieldsets = ((None, {"fields": ("name", "slug", "opportunities")}), CREATED_UPDATED)
    filter_horizontal = ("opportunities",)
    list_display = ("name", "slug", "created", "updated")
    list_filter = ("created", "updated")
    search_fields = ("name",)

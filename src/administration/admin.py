from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from administration.models import User, Organisation, Opportunity, WantToHelp, OpportunityCategory, UserProfile
from common.admin import BaseModelAdmin, SlugableModelAdmin
from common.admin_site import admin_site


@register(User, site=admin_site)
class UserAdmin(BaseUserAdmin):
    pass


@register(Group, site=admin_site)
class CustomGroupAdmin(GroupAdmin):
    pass


@register(Organisation, site=admin_site)
class OrganisationAdmin(BaseModelAdmin, SlugableModelAdmin):
    search_fields = ('name',)


@register(Opportunity, site=admin_site)
class OpportunityAdmin(BaseModelAdmin, SlugableModelAdmin):
    list_display = ('name', 'show_org_url', 'deadline', 'show_opp_url', 'description')
    list_filter = ('deadline', 'organisation')
    search_fields = ('name',)

    def show_opp_url(self, obj):
        return format_html(f"<a href='{obj.url}'>{obj.url}</a>")

    show_opp_url.short_description = "url"

    def show_org_url(self, obj):
        return format_html(f"<a href='{obj.organisation.get_absolute_url()}'>{obj.organisation.name}</a>")

    show_org_url.short_description = "organisation"


@register(WantToHelp, site=admin_site)
class WantToHelpAdmin(ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('email',)


@register(OpportunityCategory, site=admin_site)
class OpportunityCategoryAdmin(BaseModelAdmin, SlugableModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@register(UserProfile, site=admin_site)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'organisation', 'description')
    list_filter = ('organisation',)
    search_fields = ('user', 'organization')

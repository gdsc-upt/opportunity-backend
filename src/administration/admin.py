from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from administration.models import User, ExampleModel, Organisation, Partner, Faq, Opportunity, MenuItem, Article
from administration.admin_site import admin_site


class UserAdmin(BaseUserAdmin):
    pass


class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)


class OrganisationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_org_url', 'deadline', 'show_opp_url', 'description')
    list_filter = ('deadline', 'organisation')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def show_opp_url(self, obj):
        return format_html(f"<a href='{obj.url}'>{obj.url}</a>")

    show_opp_url.short_description = "url"

    def show_org_url(self, obj):
        return format_html(f"<a href='{obj.organisation.get_absolute_url()}'>{obj.organisation.name}</a>")

    show_org_url.short_description = "organisation"


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link', 'image', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'description', 'is_published', 'created')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin_site.register(ExampleModel, ExampleModelAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Partner, PartnerAdmin)
admin_site.register(Faq, FaqAdmin)
admin_site.register(Organisation, OrganisationAdmin)
admin_site.register(Opportunity, OpportunityAdmin)
admin_site.register(MenuItem, MenuItemAdmin)
admin_site.register(Article, ArticleAdmin)

from django.contrib.admin import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from administration.models import User, ExampleModel, Organisation, Partner, Article, Faq, Opportunity


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'description', 'is_published', 'created')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title', )}


@register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_org_url', 'deadline', 'show_opp_url', 'description')
    list_filter = ('deadline', 'organisation')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def show_opp_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

    show_opp_url.short_description = "url"

    def show_org_url(self, obj):
        return format_html("<a href='/api/admin/administration/organisation/{url}/change/'>{name}</a>",
                           url=obj.organisation_id, name=obj.organisation.name)

    show_org_url.short_description = "organisation"


@register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'slug', 'opportunity_categories', 'other', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('email',)
    prepopulated_fields = {'slug': ('email', )}

from django.contrib.admin import register, ModelAdmin

from common.admin import BaseModelAdmin, SlugableModelAdmin
from common.admin_site import admin_site
from website.models import Partner, Faq, MenuItem, Article, Newsletter


@register(Partner, site=admin_site)
class PartnerAdmin(BaseModelAdmin, SlugableModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name',)


@register(Faq, site=admin_site)
class FaqAdmin(BaseModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)


@register(MenuItem, site=admin_site)
class MenuItemAdmin(ModelAdmin):
    list_display = ('name', 'link', 'image', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)


@register(Article, site=admin_site)
class ArticleAdmin(BaseModelAdmin, SlugableModelAdmin):
    list_display = ('name', 'slug', 'image', 'description', 'is_published', 'created')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('title',)


@register(Newsletter, site=admin_site)
class NewsletterAdmin(BaseModelAdmin):
    list_display = ('email', 'other', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('email',)

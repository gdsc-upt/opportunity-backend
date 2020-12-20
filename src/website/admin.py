import admin_thumbnails
from django.contrib.admin import register, ModelAdmin, TabularInline

from common.admin import BaseModelAdmin, SlugableModelAdmin, CREATED_UPDATED
from common.admin_site import admin_site
from website.models import Partner, Faq, MenuItem, Article, Newsletter, WantToHelp


class CategoriesInline(TabularInline):
    model = Newsletter.categories.through
    extra = 0
    autocomplete_fields = ('category',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'


@register(Newsletter, site=admin_site)
class NewsletterAdmin(BaseModelAdmin):
    inlines = (CategoriesInline,)
    fieldsets = (
        (None, {
            'fields': ('email', 'categories', 'other')
        }),
        CREATED_UPDATED
    )
    filter_horizontal = ('categories',)
    list_display = ('email', 'get_categories', 'other', 'created')
    list_filter = ('categories', 'created', 'updated')
    search_fields = ('email', 'categories__name', 'other')

    def get_categories(self, obj: Newsletter):
        return [res["name"] for res in obj.categories.values('name')]

    get_categories.short_description = 'categories'


@admin_thumbnails.thumbnail('logo', background=True)
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


@register(WantToHelp, site=admin_site)
class WantToHelpAdmin(ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('email',)

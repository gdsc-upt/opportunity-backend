from typing import AnyStr, Tuple, List

import admin_thumbnails
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib.admin import register, ModelAdmin, TabularInline, SimpleListFilter, EmptyFieldListFilter
from django.db.models import QuerySet, Q

from common.admin import BaseModelAdmin, SlugableModelAdmin, CREATED_UPDATED, SortableModelAdmin
from common.admin_site import admin_site
from website.models import Partner, Faq, MenuItem, Article, Newsletter, WantToHelp, Contact


class MenuItemsParentFilter(SimpleListFilter):
    title = 'parent'
    parameter_name = 'parent'

    def lookups(self, request, model_admin) -> List[Tuple[int, AnyStr]]:
        queryset: QuerySet[MenuItem] = model_admin.get_queryset(request)
        return [(item.id, item.name) for item in queryset if not item.parent]

    def get_children_filter(self) -> Q:
        filters = Q(pk=0)
        for item in MenuItem.objects.filter(parent__id=self.value()):
            if children_filter := item.get_children_filter(include_self=True):
                filters |= children_filter
        return filters

    def queryset(self, request, queryset: QuerySet[MenuItem]):
        if self.value():
            return queryset.filter(self.get_children_filter())


class MenuItemInline(SortableInlineAdminMixin, TabularInline):
    model = MenuItem
    fields = ('name', 'link', 'type', 'parent')
    extra = 0
    verbose_name = 'Child'
    verbose_name_plural = 'Children'


@register(MenuItem, site=admin_site)
class MenuItemAdmin(SortableModelAdmin, ModelAdmin):
    inlines = (MenuItemInline,)

    list_display = ('name', 'link', 'type', 'parent', 'order_index')
    list_filter = (MenuItemsParentFilter, ('parent', EmptyFieldListFilter), 'type')
    list_editable = ('parent', 'type', 'link')

    search_fields = ('name',)
    autocomplete_fields = ('parent',)


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


@register(Contact, site=admin_site)
class ContactAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        CREATED_UPDATED
    )
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'subject')

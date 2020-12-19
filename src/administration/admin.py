from django.contrib.admin import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from administration.models import User, ExampleModel, Organization, Partner, Faq


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


@register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

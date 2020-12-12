from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ExampleModel, Partner


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    exclude = ('date',)


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ExampleModel, MenuItem


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    exclude = ('date',)


@register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link', 'image', 'parent')
    list_filter = ('parent', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}

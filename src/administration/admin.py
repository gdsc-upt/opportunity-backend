from django.contrib.admin import register, ModelAdmin
from django.contrib.auth import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ExampleModel


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    exclude = ('date',)

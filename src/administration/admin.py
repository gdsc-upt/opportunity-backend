from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ExampleModel, Faq


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    exclude = ('date',)


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)

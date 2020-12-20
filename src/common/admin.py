from django.contrib.admin import ModelAdmin


class BaseModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

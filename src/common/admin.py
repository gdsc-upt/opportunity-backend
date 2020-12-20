from django.contrib.admin import ModelAdmin


class BaseModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


CREATED_UPDATED = (
    'Created/Updated', {
        'classes': ('collapse',),
        'fields': ('created', 'updated',),
        'description': 'Info about the time this entry was added here or updated'
    }
)

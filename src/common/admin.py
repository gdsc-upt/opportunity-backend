from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin import ModelAdmin


class BaseModelAdmin(ModelAdmin):
    readonly_fields = ("created", "modified")


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# this function is meant to override default get_max_order if object is newly created
# noinspection PyUnusedLocal
def get_max_order(request, obj, *args, **kwargs):
    return 0


class SortableModelAdmin(SortableAdminMixin, ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            for item in self.model.objects.all():
                item.order_index += 1
                item.save()
            SortableAdminMixin.get_max_order = get_max_order
        super().save_model(request, obj, form, change)


CREATED_MODIFIED = (
    "Created / Modified",
    {
        "classes": ("collapse",),
        "fields": (
            "created",
            "modified",
        ),
        "description": "Info about the time this entry was added here or updated",
    },
)

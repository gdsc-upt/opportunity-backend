from django.db.models import Model, BooleanField, SlugField
from model_utils.models import TimeStampedModel


class PublishableModel(Model):
    is_published = BooleanField(db_index=True)

    class Meta:
        abstract = True


class SlugableModel(Model):
    slug = SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True

    def __str__(self):
        if name := getattr(self, "name", None):
            return name
        if title := getattr(self, "title", None):
            return title
        if slug := getattr(self, "slug", None):
            return slug
        if email := getattr(self, "email", None):
            return email
        return self.__class__.__name__ + " " + str(self.id)

    @property
    def change_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy(
            f"admin:{self._meta.app_label}_{self._meta.model_name}_change",
            args=[str(self.id)],
        )

    @property
    def href(self):
        """
        Use this property in admin dashboard to show this object's name as html anchor
        that redirects to object's edit page
        @return:
        """
        from django.utils.html import format_html

        return format_html(f"<a href='{self.change_url}'>{self}</a>")

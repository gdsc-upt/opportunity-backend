from django.db.models import Model, BooleanField, SlugField, DateTimeField


class PublishableModel(Model):
    is_published = BooleanField()

    class Meta:
        abstract = True


class SlugableModel(Model):
    slug = SlugField(primary_key=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel(Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

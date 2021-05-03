from django.db.models import QuerySet
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ALL_FIELDS

from common.constants import ID, QUESTION, ANSWER, CREATED, MODIFIED, PARENT
from website.models import (
    WantToHelp,
    Faq,
    Partner,
    MenuItem,
    Article,
    Newsletter,
    Contact,
    Setting,
)


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ALL_FIELDS


class FaqSerializer(ModelSerializer):
    class Meta:
        fields = ID, QUESTION, ANSWER
        model = Faq


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ALL_FIELDS


class MenuItemSerializer(ModelSerializer):
    children = SerializerMethodField("get_children")

    @staticmethod
    def get_children(menu_item: MenuItem):
        queryset: QuerySet[MenuItem] = MenuItem.objects.filter(parent=menu_item)
        serializer = MenuItemSerializer(instance=queryset, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = MenuItem
        exclude = (PARENT, ID)


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ALL_FIELDS


class WantToHelpSerializer(ModelSerializer):
    class Meta:
        model = WantToHelp
        fields = ALL_FIELDS


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = CREATED, MODIFIED, ID


class SettingSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = ALL_FIELDS

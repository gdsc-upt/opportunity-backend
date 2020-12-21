from rest_framework.serializers import ModelSerializer

from administration.serializers import CategorySerializer
from website.models import Faq, Partner, MenuItem, Article, Newsletter, WantToHelp, Contact


class NewsletterSerializer(ModelSerializer):
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Newsletter
        fields = '__all__'


class FaqSerializer(ModelSerializer):
    class Meta:
        fields = 'id', 'question', 'answer'
        model = Faq


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class WantToHelpSerializer(ModelSerializer):
    class Meta:
        model = WantToHelp
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contact

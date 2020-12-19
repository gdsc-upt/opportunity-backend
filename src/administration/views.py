from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets

from administration.models import Partner, ExampleModel, Faq, Organisation, MenuItem, Article
from administration.serializers import PartnerSerializer, ExampleModelSerializer, FaqSerializer, OrganizationSerializer, MenuItemSerializer, \
    ArticleSerializer


class ExampleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleModelSerializer
    queryset = ExampleModel.objects.all()


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.filter(is_published=True)


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class MenuItemViewSet(ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_published=True)

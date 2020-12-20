from rest_framework.viewsets import ReadOnlyModelViewSet

from website.models import Partner, Faq, MenuItem, Article, Newsletter
from website.serializers import PartnerSerializer, FaqSerializer, MenuItemSerializer, ArticleSerializer, NewsletterSerializer


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.filter(is_published=True)


class MenuItemViewSet(ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_published=True)


class NewsletterViewSet(ReadOnlyModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()

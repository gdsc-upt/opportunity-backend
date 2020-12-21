from django.db.models import QuerySet
from django.http import Http404
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from website.models import Partner, Faq, MenuItem, Article, Newsletter, WantToHelp, Contact
from website.serializers import PartnerSerializer, FaqSerializer, MenuItemSerializer, ArticleSerializer, \
    NewsletterSerializer, WantToHelpSerializer, ContactSerializer


class NewsletterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.filter(is_published=True)


class MenuItemViewSet(ListModelMixin, GenericViewSet):
    serializer_class = MenuItemSerializer
    queryset: QuerySet[MenuItem] = MenuItem.objects.filter(parent__exact=None)

    def get_object(self):
        obj: MenuItem = super(MenuItemViewSet, self).get_object()
        if obj.parent:
            raise Http404
        return obj


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_published=True)


class WantToHelpViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = WantToHelpSerializer
    queryset = WantToHelp.objects.all()


class ContactViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

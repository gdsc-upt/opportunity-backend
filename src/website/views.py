from django.core.mail import send_mail
from django.db.models import QuerySet
from django.http import Http404
from rest_framework import permissions
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
    permission_classes = [permissions.AllowAny]


class ContactViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        res = super(ContactViewSet, self).create(request, *args, **kwargs)
        if res.status_code == 201:
            name = request.data["name"]
            email = request.data["email"]
            subject = request.data["subject"]
            message = request.data["message"]
            send_mail(subject, "From: " + name + ", " + email + "\n" + message, "testbackendemail001@gmail.com",
                      ["mail1@mailinator.com"])
            send_mail("Submit Opportunity", "Iti multumim ca ne-ai contactat!", "testbackendemail001@gmail.com",
                      [email])
            print(request)
        return res

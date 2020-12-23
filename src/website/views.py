from django.conf import settings
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.http import Http404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
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


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_id='Add message',
        operation_description='Saves messages to database and sends email both to the one that submitted form and to the team\'s email',
        operation_summary='Send messages to Opportunity team',
        security=[],
        responses={
            status.HTTP_201_CREATED: ContactSerializer(),
        },
        tags=['Contact']
    ))
class ContactViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        res = super(ContactViewSet, self).create(request, *args, **kwargs)
        if res.status_code == 201 and not settings.DEBUG:
            email = res.data["email"]
            subject = res.data["subject"]
            message = f"From: {res.data['name']}, {email}\n{res.data['message']}"
            send_mail(subject, message, None, ["mail1@mailinator.com"])
            send_mail("Submit Opportunity", "Îţi mulţumim că ne-ai contactat!", None, [email])
        if res.status_code == 201 and settings.DEBUG:
            print(f"From: {res.data['name']}, {res.data['email']}\n{res.data['message']}")
        return res

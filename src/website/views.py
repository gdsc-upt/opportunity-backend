from django.conf import settings
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.http import Http404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from website.models import (
    Partner,
    Faq,
    Article,
    Newsletter,
    WantToHelp,
    Contact,
    Setting,
    MenuItem,
)
from website.serializers import (
    PartnerSerializer,
    FaqSerializer,
    MenuItemSerializer,
    ArticleSerializer,
    NewsletterSerializer,
    WantToHelpSerializer,
    ContactSerializer,
    SettingSerializer,
)


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

    def get_object(self) -> MenuItem:
        obj: MenuItem = super().get_object()
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


@extend_schema_view(
    create=extend_schema(
        description="Saves messages to database and sends email "
        "both to the one that submitted form and to the team's email",
        summary="Send messages to Opportunity team",
        auth=[],
        responses={
            status.HTTP_201_CREATED: ContactSerializer,
        },
    )
)
class ContactViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        if res.status_code == 201 and not settings.DEBUG:
            email = res.data["email"]
            subject = res.data["subject"]
            message = f"From: {res.data['name']}, {email}\n{res.data['message']}"
            send_mail(subject, message, None, ["mail1@mailinator.com"])
            send_mail(
                "Submit Opportunity", "Îţi mulţumim că ne-ai contactat!", None, [email]
            )
        if res.status_code == 201 and settings.DEBUG:
            print(
                f"From: {res.data['name']}, {res.data['email']}\n{res.data['message']}"
            )
        return res


class SettingViewSet(ReadOnlyModelViewSet):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
    lookup_field = "slug"

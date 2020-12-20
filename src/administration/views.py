from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets

from administration.models import Partner, ExampleModel, Faq, Organisation, MenuItem, Article, Newsletter, WantToHelp, OpportunityCategory, \
    UserProfile
from administration.serializers import PartnerSerializer, ExampleModelSerializer, FaqSerializer, OrganizationSerializer, MenuItemSerializer, \
    ArticleSerializer, NewsletterSerializer, WantToHelpSerializer, OpportunityCatSerializer, UserProfileSerializer


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


class NewsletterViewSet(ReadOnlyModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.filter(is_published=True)


class WantToHelpViewSet(ReadOnlyModelViewSet):
    queryset = WantToHelp.objects.all()
    serializer_class = WantToHelpSerializer


class OpportunityCatViewSet(ReadOnlyModelViewSet):
    serializer_class = OpportunityCatSerializer
    queryset = OpportunityCategory.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

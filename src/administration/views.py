from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets

from administration.models import Partner, ExampleModel, Faq, Organization
from administration.serializers import PartnerSerializer, ExampleModelSerializer, FaqSerializer, OrganizationSerializer


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
    queryset = Organization.objects.filter(is_published=True)

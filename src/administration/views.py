from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from administration.models import Partner
from administration.serializers import PartnerSerializer


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

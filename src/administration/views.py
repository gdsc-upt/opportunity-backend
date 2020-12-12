from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from administration.models import Organization
from administration.serializers import OrganizationSerializer


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

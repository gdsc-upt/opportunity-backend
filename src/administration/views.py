from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import ExampleModel
from .serializers import ExampleModelSerializer


class ExampleModelViewSet(viewsets.ModelViewSet):

    serializer_class = ExampleModelSerializer
    queryset = ExampleModel.objects.all()

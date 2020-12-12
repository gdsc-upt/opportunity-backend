from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from administration.models import News
from administration.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


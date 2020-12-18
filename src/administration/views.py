from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets

from administration.models import Partner, ExampleModel, Faq, News
from administration.serializers import PartnerSerializer, ExampleModelSerializer, FaqSerializer, NewsSerializer


class ExampleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleModelSerializer
    queryset = ExampleModel.objects.all()


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.filter(is_published=True)


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


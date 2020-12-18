from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Faq
from administration.serializers import FaqSerializer


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.filter(is_published=True)

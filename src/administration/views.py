from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Partner
from administration.serializers import PartnerSerializer


class PartnerViewSet(ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

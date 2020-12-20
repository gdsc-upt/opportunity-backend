from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Organisation, WantToHelp, OpportunityCategory, UserProfile
from administration.serializers import OrganizationSerializer, WantToHelpSerializer, OpportunityCatSerializer, UserProfileSerializer


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class WantToHelpViewSet(ReadOnlyModelViewSet):
    queryset = WantToHelp.objects.all()
    serializer_class = WantToHelpSerializer


class OpportunityCatViewSet(ReadOnlyModelViewSet):
    serializer_class = OpportunityCatSerializer
    queryset = OpportunityCategory.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Organisation, Category, UserProfile
from administration.serializers import OrganizationSerializer, CategorySerializer, UserProfileSerializer


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Organisation, Category, UserProfile, Opportunity
from administration.serializers import (
    OrganizationSerializer,
    CategorySerializer,
    UserProfileSerializer,
    OpportunitySerializer,
)


@extend_schema_view(
    create=extend_schema(
        operation_id="Create new opportunity",
        description="Opportunities endpoint description",
        summary="Opportunities endpoint summary",
        responses={
            status.HTTP_200_OK: OpportunitySerializer,
        },
    ),
    list=extend_schema(
        operation_id="Get all published opportunities",
        description="Opportunities endpoint description",
        summary="Opportunities endpoint summary",
        responses={
            status.HTTP_200_OK: OpportunitySerializer(many=True),
        },
    ),
)
class OpportunityViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = OpportunitySerializer
    queryset = Opportunity.objects.filter(is_published=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

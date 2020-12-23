from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import Organisation, Category, UserProfile, Opportunity
from administration.serializers import OrganizationSerializer, CategorySerializer, UserProfileSerializer, OpportunitySerializer


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_id='Create new opportunity',
    operation_description='Opportunities endpoint description',
    operation_summary='Opportunities endpoint summary',
    responses={status.HTTP_200_OK: OpportunitySerializer(), status.HTTP_404_NOT_FOUND: 'Not found'}))
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_id='Get all published opportunities',
    operation_description='Opportunities endpoint description',
    operation_summary='Opportunities endpoint summary',
    responses={status.HTTP_200_OK: OpportunitySerializer(many=True), status.HTTP_404_NOT_FOUND: 'Not found'}))
class OpportunityViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = OpportunitySerializer
    queryset = Opportunity.objects.filter(is_published=True)


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

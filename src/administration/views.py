from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from administration.models import Organisation, Category, UserProfile, Opportunity
from administration.serializers import (
    OrganizationSerializer,
    CategorySerializer,
    UserProfileSerializer,
    OpportunitySerializer,
    UserSerializer,
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
    permission_classes = [permissions.AllowAny]


class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organisation.objects.filter(is_published=True)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UserProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        Token.objects.filter(user=user).delete()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.USERNAME, "email": user.EMAIL})


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]  # Or anon users can't register
    serializer_class = UserSerializer

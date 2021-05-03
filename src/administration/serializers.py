from rest_framework.serializers import ModelSerializer

from administration.models import Organisation, Category, UserProfile, Opportunity
from common.constants import CREATED, MODIFIED, NAME, SLUG, ID


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class OrganizationLightSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = NAME, SLUG


class OpportunitySerializer(ModelSerializer):
    organisation = OrganizationLightSerializer(read_only=True, many=True)

    class Meta:
        model = Opportunity
        exclude = (MODIFIED, ID)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = (CREATED, MODIFIED)
        depth = 1


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

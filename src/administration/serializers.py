from rest_framework.serializers import ModelSerializer

from administration.models import Organisation, Category, UserProfile, Opportunity


class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        exclude = ("modified",)
        depth = 1


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ("created", "modified")
        depth = 1


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

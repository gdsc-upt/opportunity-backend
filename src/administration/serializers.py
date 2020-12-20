from rest_framework import serializers

from administration.models import Organisation, WantToHelp, OpportunityCategory, UserProfile


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class WantToHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantToHelp
        fields = '__all__'


class OpportunityCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityCategory
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

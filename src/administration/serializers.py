from rest_framework.serializers import ModelSerializer

from administration.models import Organisation, Category, UserProfile


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created', 'updated')
        depth = 1


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

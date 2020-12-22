from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from administration.models import Organisation, Category, UserProfile, Opportunity, User


class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        exclude = ('updated',)
        depth = 1


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


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

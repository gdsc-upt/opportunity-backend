from rest_framework import serializers

from administration.models import ExampleModel, Partner, Faq, Organization


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('name', 'email', 'date', 'age')


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'id', 'question', 'answer'
        model = Faq


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


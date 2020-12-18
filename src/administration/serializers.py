from rest_framework import serializers

from administration.models import ExampleModel, Partner, Faq


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

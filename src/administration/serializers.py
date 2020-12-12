from rest_framework import serializers

from .models import ExampleModel
from .models import News

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ExampleModel
        fields = ('name','email','date','age')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
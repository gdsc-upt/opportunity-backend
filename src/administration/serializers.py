from rest_framework import serializers

from .models import ExampleModel

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ExampleModel
        fields = ('name','email','date','age')

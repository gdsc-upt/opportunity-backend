from rest_framework import serializers

from administration.models import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'id', 'question', 'answer'
        model = Faq

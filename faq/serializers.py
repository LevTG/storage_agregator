from rest_framework import serializers
from .models import Faq


class FAQRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "question",
            "answer"
        ]

    def create(self, validated_data):
        faq = Faq(**validated_data)
        faq.save()
        return faq


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "question",
            "answer"
        ]
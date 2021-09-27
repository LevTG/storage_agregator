from rest_framework import serializers
from .models import StorageFeedback


class AnswerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            "text"
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            'id',
            "text",
            'created_on',
        ]


class StorageFeedbackRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            "text",
            "rating",
            "username",
            'email',
            'phone_number',
            "text",
            'status'
        ]


class StorageFeedbackSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()

    class Meta:
        model = StorageFeedback
        fields = [
            'id',
            "rating",
            "username",
            'email',
            'phone_number',
            "text",
            'answer',
            'status',
            'created_on',
        ]


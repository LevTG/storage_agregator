from rest_framework import serializers
from .models import StorageFeedback
from storages.models import Storage


class StorageFeedbackRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            "text",
            "grade",
            "author",
            "text"
        ]


class StorageFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            'id',
            "grade",
            "author",
            "text",
            "storage",
            'status',
        ]

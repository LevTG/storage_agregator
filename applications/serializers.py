from rest_framework import serializers
from .models import Application
from storages.models import Storage


class ApplicationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            "name",
            "email",
            "phone_number",
            "text",
            'storage',
            'recipient'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            "name",
            "email",
            "phone_number",
            "text",
            "storage",
            'status',
            'recipient'
        ]
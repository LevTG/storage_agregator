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
            'recipient',
            'date_carry'
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
            'date_carry'
        ]
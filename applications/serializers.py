from rest_framework import serializers
from .models import Application
from storages.models import Storage


class ApplicationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "name",
            "email",
            "phone_number",
            "text"
        ]

    def create(self, validated_data):
        try:
            application = Application(**validated_data)
            application.save()
            return application
        except Exception as e:
            raise e


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "name",
            "email",
            "phone_number",
            "text",
            "storage"
        ]
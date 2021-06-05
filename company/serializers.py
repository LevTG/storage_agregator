from rest_framework import serializers
from .models import Company


class CompanyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "city",
            "is_private",
            "owner"
        ]

    def create(self, validated_data):
        try:
            company = Company(**validated_data)
            company.save()
            return company
        except Exception as e:
            raise e


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "city"
        ]
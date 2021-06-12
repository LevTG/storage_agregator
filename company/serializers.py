from rest_framework import serializers
from .models import Company

from storages.serializers import StorageSerializer


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'id',
            "name",
            "city"
        ]


class SingleCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            "name",
            "city",
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        company = Company.objects.create(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.owner.username != user.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this company."})
        return super(self).update(instance, validated_data)

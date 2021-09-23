from rest_framework import serializers
from .models import Company

from storages.serializers import StorageSerializer
from images.serializers import ImageSerializer


class CompanySerializer(serializers.ModelSerializer):
    logo = ImageSerializer(required=False)
    owner = serializers.CharField(source='owner.username', required=False)

    class Meta:
        model = Company
        fields = [
            'id',
            "name",
            "city",
            'description',
            'logo',
            'company_url',
            'storage_count',
            'owner'
        ]


class CompanyRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'id',
            'owner',
            'description',
            "name",
            "city",
            'company_url',
            'is_private'
        ]

    def create(self, validated_data):
        if 'owner' not in validated_data.keys():
            user = self.context['request'].user
            validated_data['owner'] = user.id
        company = Company.objects.create(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.owner.username != user.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this company."})
        return super(self).update(instance, validated_data)

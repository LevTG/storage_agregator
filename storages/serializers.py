from rest_framework import serializers

from images.serializers import ImageAlbumSerializer
from .models import Storage


class StorageRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate',
        ]
        extra_kwargs = {
            'company_owner': {'required': True},
            'address': {'required': True},
        }


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate'
        ]


class SingleStorageSerializer(serializers.ModelSerializer):
    album = ImageAlbumSerializer()

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate'
        ]

    def create(self, validated_data):
        company = Storage.objects.create(**validated_data)
        company.save()

        return company

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.company_owner.owner.username != user.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this company."})
        return super(self).update(instance, validated_data)


class StorageSerializer(serializers.ModelSerializer):
    album = ImageAlbumSerializer()

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate',
            'album'
        ]

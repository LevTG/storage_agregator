from rest_framework import serializers

from images.serializers import ImageAlbumSerializer
from .models import Storage


class StorageRegistrationSerializer(serializers.ModelSerializer):
    # album = ImageAlbumSerializer()

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'owner',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate'

        ]
        extra_kwargs = {
            'owner': {'required': True},
            'address': {'required': True},
        }


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'owner',
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
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'owner',
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
        if instance.owner.owner.username != user.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this company."})
        return super(self).update(instance, validated_data)

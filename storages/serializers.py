from rest_framework import serializers
from .models import Storage


class StorageRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'address',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate',
        ]

    def create(self, validated_data):
        if validated_data['address'] is None:
            raise serializers.ValidationError(
                {"address": "Address must be filled"})
        storage = Storage(**validated_data)
        storage.save()
        return storage


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'address',
            'description',
            'square',
            'price',
            'access',
            'work_hours_start',
            'work_hours_end',
            'surveillance',
            'climate',
        ]
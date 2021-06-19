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
            'work_hours_start',
            'work_hours_end',
            'video_surveillance',
            'storage_type',
            'warehouse_type',
            'access_24h',
            'mobile_app',
            'clever_lock',
            'cleaning',
            'online_contract',
            'ventilation',
            'shipping',
            'wrapping',
            'straight_way',
            'any_rental_period',
            'inventoty',
            'inshurance'
        ]
        extra_kwargs = {
            'company_owner': {'required': True},
            'address': {'required': True},
        }


class StorageSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'work_hours_start',
            'work_hours_end',
            'video_surveillance',
            'storage_type',
            'warehouse_type',
            'access_24h',
            'mobile_app',
            'clever_lock',
            'cleaning',
            'online_contract',
            'ventilation',
            'shipping',
            'wrapping',
            'straight_way',
            'any_rental_period',
            'inventoty',
            'inshurance',
            'album'
        ]

    def get_album(self, obj):
        return ImageAlbumSerializer(obj.album, context=self.context).data


class SingleStorageSerializer(serializers.ModelSerializer):
    album = ImageAlbumSerializer()

    class Meta:
        model = Storage
        fields = [
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'work_hours_start',
            'work_hours_end',
            'video_surveillance',
            'storage_type',
            'warehouse_type',
            'access_24h',
            'mobile_app',
            'clever_lock',
            'cleaning',
            'online_contract',
            'ventilation',
            'shipping',
            'wrapping',
            'straight_way',
            'any_rental_period',
            'inventoty',
            'inshurance'
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

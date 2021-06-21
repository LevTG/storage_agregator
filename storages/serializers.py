from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from images.serializers import ImageAlbumSerializer
from .models import Storage, WAREHOUSE_TYPE, STORAGE_TYPE


class StorageRegistrationSerializer(serializers.ModelSerializer):
    warehouse_type = MultipleChoiceField(choices=WAREHOUSE_TYPE, allow_blank=True)
    storage_type = MultipleChoiceField(choices=STORAGE_TYPE, allow_blank=True)

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
            'inventory',
            'inshurance'
        ]
        extra_kwargs = {
            'company_owner': {'required': True},
            'address': {'required': True},
        }


class StorageSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()
    warehouse_type = MultipleChoiceField(choices=WAREHOUSE_TYPE)
    storage_type = MultipleChoiceField(choices=STORAGE_TYPE)

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
            'inventory',
            'inshurance',
            'album'
        ]

    def get_album(self, obj):
        return ImageAlbumSerializer(obj.album, context=self.context).data


class SingleStorageSerializer(serializers.ModelSerializer):
    album = ImageAlbumSerializer()
    warehouse_type = MultipleChoiceField(choices=WAREHOUSE_TYPE)
    storage_type = MultipleChoiceField(choices=STORAGE_TYPE)

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
            'inventory',
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

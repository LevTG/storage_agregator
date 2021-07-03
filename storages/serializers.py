from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from images.serializers import ImageAlbumSerializer
from metro.serializers import StationLineSerializer
from .models import Storage, WAREHOUSE_TYPE, STORAGE_TYPE


class ServiceSerializer(serializers.Serializer):
    video_surveillance = serializers.BooleanField(allow_null=True, required=False)
    access_24h = serializers.BooleanField(allow_null=True, required=False)
    mobile_app = serializers.BooleanField(allow_null=True, required=False)
    clever_lock = serializers.BooleanField(allow_null=True, required=False)
    cleaning = serializers.BooleanField(allow_null=True, required=False)
    online_contract = serializers.BooleanField(allow_null=True, required=False)
    ventilation = serializers.BooleanField(allow_null=True, required=False)
    shipping = serializers.BooleanField(allow_null=True, required=False)
    wrapping = serializers.BooleanField(allow_null=True, required=False)
    straight_way = serializers.BooleanField(allow_null=True, required=False)
    any_rental_period = serializers.BooleanField(allow_null=True, required=False)
    inventory = serializers.BooleanField(allow_null=True, required=False)
    inshurance = serializers.BooleanField(allow_null=True, required=False)


# По какой-то причине данные попадающие в serializer multichoiceField дополнительно оборачиваются листом. И все ломается
# Для этого создала этот CustomField

class CustomMultipleChoiceField(serializers.MultipleChoiceField):
    def to_internal_value(self, data):
        if isinstance(data, str) or not hasattr(data, '__iter__'):
            self.fail('not_a_list', input_type=type(data).__name__)
        if not self.allow_empty and len(data) == 0:
            self.fail('empty')
        # Вот отличающаяся строка
        data = data[0]
        #########################
        return {
            super(MultipleChoiceField, self).to_internal_value(item)
            for item in data
        }


class StorageRegistrationSerializer(serializers.ModelSerializer):
    warehouse_type = CustomMultipleChoiceField(choices=WAREHOUSE_TYPE, allow_blank=True)
    storage_type = CustomMultipleChoiceField(choices=STORAGE_TYPE, allow_blank=True)

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
            'storage_type',
            'warehouse_type',
            'city',
            'longitude',
            'latitude',

            'video_surveillance',
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
    album = serializers.SerializerMethodField(required=False)
    warehouse_type = CustomMultipleChoiceField(choices=WAREHOUSE_TYPE, required=False)
    storage_type = CustomMultipleChoiceField(choices=STORAGE_TYPE, required=False)
    metro = StationLineSerializer(many=True, required=False)
    services = ServiceSerializer(required=False)

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_owner',
            'description',
            'square',
            'price',
            'metro',
            'work_hours_start',
            'work_hours_end',
            'warehouse_type',
            'storage_type',
            'city',
            'longitude',
            'latitude',
            'album',
            'services'
        ]

    def get_album(self, obj):
        return ImageAlbumSerializer(obj.album, context=self.context).data

    def create(self, validated_data):
        return super(StorageSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.company_owner.owner.username != user.username:
            raise serializers.ValidationError({"authorize": "You dont have permission for this company."})
        services = ServiceSerializer(data=validated_data.pop('services', {}), partial=True)
        validated_data['company_owner'] = validated_data.pop('company_id')
        if services.is_valid():
            for attr, value in services.validated_data.iteritems():
                setattr(instance, attr, value)
        return super(self).update(instance, validated_data)


class StorageUpdateSerializer(serializers.ModelSerializer):
    warehouse_type = CustomMultipleChoiceField(choices=WAREHOUSE_TYPE, required=False)
    storage_type = CustomMultipleChoiceField(choices=STORAGE_TYPE, required=False)
    metro = StationLineSerializer(many=True, required=False)
    services = ServiceSerializer(required=False)

    class Meta:
        model = Storage
        fields = [
            'address',
            'description',
            'square',
            'price',
            'metro',
            'work_hours_start',
            'work_hours_end',
            'warehouse_type',
            'storage_type',
            'city',
            'longitude',
            'latitude',
            'services'
        ]

# class SingleStorageSerializer(serializers.ModelSerializer):
#     album = ImageAlbumSerializer()
#     warehouse_type = MultipleChoiceField(choices=WAREHOUSE_TYPE)
#     storage_type = MultipleChoiceField(choices=STORAGE_TYPE)
#     services = ServiceSerializer()
#
#     class Meta:
#         model = Storage
#         fields = [
#             'address',
#             'company_owner',
#             'description',
#             'square',
#             'price',
#             'metro',
#             'work_hours_start',
#             'work_hours_end',
#             'storage_type',
#             'warehouse_type',
#             'album',
#             'services'
#         ]

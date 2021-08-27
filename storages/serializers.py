from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from images.serializers import ImageAlbumSerializer
from metro.serializers import StationLineSerializer, station_get_or_create
from .models import Storage, Manager, WAREHOUSE_TYPE, STORAGE_TYPE


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


class SocialSerializer(serializers.Serializer):
    vk = serializers.CharField(allow_null=True, required=False)
    ok = serializers.CharField(allow_null=True, required=False)
    instagram=serializers.CharField(allow_null=True, required=False)


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
            'phone_number',
            'email',

            'square',
            'price',
            'work_hours_start',
            'work_hours_end',
            'storage_type',
            'warehouse_type',
            'city',

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
            'inshurance',

            'vk',
            'ok',
            'instagram',
            'facebook'
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
    social = SocialSerializer(required=False)
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()

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
            'album',
            'latitude',
            'longitude',
            'services',
            'social'
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
        social = SocialSerializer(data=validated_data.pop('social', {}), partial=True)

        validated_data['company_owner'] = validated_data.pop('company_id')

        if services.is_valid():
            for attr, value in services.validated_data.iteritems():
                setattr(instance, attr, value)

        if social.is_valid():
            for attr, value in social.validated_data.iteritems():
                setattr(instance, attr, value)

        return super(self).update(instance, validated_data)


class StorageUpdateSerializer(serializers.ModelSerializer):
    warehouse_type = CustomMultipleChoiceField(choices=WAREHOUSE_TYPE, required=False)
    storage_type = CustomMultipleChoiceField(choices=STORAGE_TYPE, required=False)
    metro = StationLineSerializer(many=True, required=False)
    services = ServiceSerializer(required=False)
    social = SocialSerializer(required=False)

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
            'status',
            'services',
            'social'
        ]

    # def update_or_create_metro(self, stations):
    #     metro_ids = []
    #     for metro in stations:
    #         station = station_get_or_create(metro)
    #         metro_ids.append(station.id)
    #     return metro_ids
    #
    # def create(self, validated_data):
    #     metro = validated_data.pop('metro', [])
    #     storage = Storage.objects.create(**validated_data)
    #     storage.metro.set(self.update_or_create_metro(metro))
    #     storage.save()
    #     return storage
    #
    # def update(self, instance, validated_data):
    #     metro = validated_data.pop('metro', [])
    #     instance.metro.set(self.update_or_create_metro(metro))
    #     instance.save()
    #     return instance

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


class StorageCoordinatesSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(source='location.x')
    longitude = serializers.FloatField(source='location.y')

    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'price',
            'latitude',
            'longitude'
        ]


class ManagerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = [
            'first_name',
            'last_name',
            'telegram_id'
        ]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = [
            'first_name',
            'last_name',
            'telegram_id'
        ]

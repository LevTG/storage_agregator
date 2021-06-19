from rest_framework import serializers
from .models import ImageAlbum, Image


class ImageRegisterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'image',
            'album',
            'name'
        ]

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'image'
        ]


class ImageAlbumRegisterSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = ImageAlbum
        fields = [
            'images'
        ]


class ImageAlbumSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = ImageAlbum
        fields = [
            'images'
        ]

    def get_images(self, obj):
        return ImageSerializer(obj.images, many=True, context=self.context).data


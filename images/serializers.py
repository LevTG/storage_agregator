from rest_framework import serializers
from .models import ImageAlbum, Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'image',
            'name',
        ]


class ImageAlbumSerializer:
    images = ImageSerializer(source='images', many=True)

    class Meta:
        model = ImageAlbum

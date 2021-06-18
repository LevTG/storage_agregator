from rest_framework import serializers
from .models import ImageAlbum, Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'name',
            'image',
            'url',
            'album'
        ]



class ImageUrlSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'image'
        ]

class ImageAlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = ImageAlbum
        fields = [
            'images'
        ]

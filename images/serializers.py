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
    #image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            'id',
            'image'
        ]
    
#    def get_image(self, obj):
#        request = self.context.get('request')
#        photo_url = obj.image.url
#        return request.build_absolute_uri(photo_url)


class ImageAlbumRegisterSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = ImageAlbum
        fields = [
            'id',
            'images'
        ]


class ImageAlbumSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = ImageAlbum
        fields = [
            'id',
            'images'
        ]

    def get_images(self, obj):
        return ImageSerializer(obj.images, many=True, context=self.context).data

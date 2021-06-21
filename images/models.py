from django.db import models
from rest_framework import fields

CATEGORY_TYPE = (('s', 'storage'), ('c', 'company'))


def get_upload_path(instance, filename):
    name = instance.name
    return f'{name}/images/{filename}'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    category = models.CharField(max_length=1, choices=CATEGORY_TYPE)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

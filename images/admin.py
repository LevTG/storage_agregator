from django.contrib import admin

from .models import ImageAlbum, Image


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', )
    fields = ['image_set']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ['name', 'image', 'album']

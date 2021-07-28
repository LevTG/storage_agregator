import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import ImageAlbum, Image
from .serializers import ImageSerializer, ImageRegisterSerializer, ImageAlbumSerializer, ImageAlbumRegisterSerializer

from storages.views import image_re


class ImageAlbumView(CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = ImageAlbum

    def post(self, req, *args, **kwargs):
        album_id = kwargs['album_id']
        albums = ImageAlbum.objects.filter(id=album_id)
        if not albums.exists():
            return Response('Error: Album with this id doesn\'t exist', status=status.HTTP_404_NOT_FOUND)
        album = albums.first()
        try:
            for key, value in req.data.items():
                if image_re.search(key):
                    form_data = {'album': album.id, 'image': value,
                                 'name': '{}'.format(uuid.uuid4), 'category': 's'}

                    image_serializer = ImageRegisterSerializer(data=form_data)

                    if not image_serializer.is_valid():
                        return Response(image_serializer.errors, status=status.HTTP_200_OK)
                    image = image_serializer.save()

        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(album.id, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class ImageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = ImageAlbumSerializer
    renderer_classes = [JSONRenderer]
    queryset = ImageAlbum.objects.all()

    def delete(self, *args, **kwargs):
        image_id = kwargs['image_id']
        images = Image.objects.filter(id=image_id)
        if images.exists():
            image = images.first()
            image.delete()
        return Response(status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})

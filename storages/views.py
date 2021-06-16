from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .serializers import StorageRegistrationSerializer, SingleStorageSerializer
from .models import Storage
from images.serializers import ImageSerializer
from images.models import ImageAlbum


class StorageRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StorageRegistrationSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser,)

    def post(self, req):
        data = req.data.copy()
        data['company_owner'] = data['company_id']
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        storage = serializer.save()
        album = ImageAlbum.objects.create()
        album.save()
        storage.album = album
        try:
            if 'images' in req.data.keys():

                form_data = {}

                for image in req.FILES.getlist('images'):

                    form_data['album'] = album.id
                    form_data['image'] = image
                    form_data['name'] = 'storage'

                    image_serializer = ImageSerializer(data=form_data)

                    if not image_serializer.is_valid():
                        return Response(image_serializer.errors, status=status.HTTP_200_OK)
                    image = image_serializer.save()
                storage.save()
        except Exception as e:
            storage.delete()
            album.delete()
            raise Exception()
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(storage.id, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class StorageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SingleStorageSerializer
    renderer_classes = [JSONRenderer]
    queryset = Storage.objects.all()
import os
import re
import uuid
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer

from .models import Storage
from .filters import StorageFilter
from .serializers import StorageRegistrationSerializer, StorageSerializer
from images.serializers import ImageRegisterSerializer
from images.models import ImageAlbum
from metro.serializers import station_get_or_create


import requests


image_re = re.compile('image\d+')


class StorageRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StorageRegistrationSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser,)

    def post(self, req, **kwargs):
        data = req.data.copy()
        metro_data = json.loads(data.pop('metro')[0])

        data['company_owner'] = data['company_id']

        services = json.loads(data.pop('services')[0])
        data.update(services)

        data['storage_type'] = json.loads(data.pop('storage_type')[0])
        data['warehouse_type'] = json.loads(data.pop('warehouse_type')[0])

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        storage = serializer.save()

        for station_data in metro_data:
            station = station_get_or_create(station_data)
            storage.metro.add(station)
        storage.save()

        album = ImageAlbum.objects.create()
        album.save()
        storage.album = album
        try:
            for key, value in req.data.items():
                if image_re.search(key):
                    form_data = {'album': album.id, 'image': value,
                                 'name': '{}'.format(uuid.uuid4), 'category': 's'}

                    image_serializer = ImageRegisterSerializer(data=form_data)

                    if not image_serializer.is_valid():
                        return Response(image_serializer.errors, status=status.HTTP_200_OK)
                    image = image_serializer.save()

            storage.save()
        except Exception as e:
            storage.delete()
            album.delete()
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(storage.id, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class StorageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]
    queryset = Storage.objects.all()


class FilterStoragesView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]
    ordering_fields = ('price', 'square')
    filterset_class = StorageFilter


class GetNearbyStorages(ListAPIView):
    pass
    # Send request to yandex_api
    'https: // geocode - maps.yandex.ru / 1.x\
    ? geocode = {0}\
    & apikey = {1}\
    & [sco = < string >]\
    & [kind = < string >]\
    & [rspn = < boolean >]\
    & [ll = < number >, < number >]\
    & [spn = < number >, < number >]\
    & [bbox = < number >, < number > ~ < number >, < number >]\
    & [format = json]\
    & [results = < integer >]\
    & [skip = < integer >]\
    & [lang = < string >]\
    & [callback = < string >]'.format('', os.environ.get("API_KEY"))

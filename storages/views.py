import os
import re
import uuid
import json

from django.contrib.gis.measure import D

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from .models import Storage
from .filters import StorageFilter
from .serializers import StorageRegistrationSerializer, StorageSerializer, StorageUpdateSerializer
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

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = StorageUpdateSerializer
            kwargs['data'] = kwargs['data'].copy()
            if 'warehouse_type' in kwargs['data'].keys():
                kwargs['data']['warehouse_type'] = json.loads(kwargs['data']['warehouse_type'])
            if 'storage_type' in kwargs['data'].keys():
                kwargs['data']['storage_type'] = json.loads(kwargs['data']['storage_type'])
            if 'metro' in kwargs['data'].keys():
                kwargs['data']['metro'] = json.loads(kwargs['data']['metro'])
            kwargs['partial'] = True
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class FilterStoragesView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]
    ordering_fields = ('price', 'square')
    filterset_class = StorageFilter
    pagination_class = PageNumberPagination

    def get_count(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.count()

    def list(self, req, **kwargs):
        response = super(FilterStoragesView, self).list(self, req)
        response.data['count'] = self.get_count()
        return response


class GetAllCities(ListAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        cities = Storage.objects.values_list('city', flat=True).order_by('city').distinct()
        data = {'city': cities}
        return Response(data, status=status.HTTP_200_OK)


class GetAllStoragesMap(ListAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        storages = Storage.objects.values('id', 'address', 'latitude', 'longitude', 'description').distinct()
        return Response(storages, status=status.HTTP_200_OK)


class GetNearbyStoragesMap(ListAPIView):
    queryset = Storage.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]


    def get(self, req, **kwargs):
       #  user_location =
       # storages = self.queryset.filter(location__dwithin=(user_location, D(km=10)))
        pass
import os
import re
import uuid
import json
import math

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from .models import Storage
from .filters import StorageFilter
from .serializers import *
from images.serializers import ImageRegisterSerializer
from images.models import ImageAlbum
from metro.serializers import station_get_or_create
from feedback.serializers import StorageFeedbackSerializer

#import os, sys
#sys.path.append('/home/backy/tgbot')
from tgbot.telegram_bot import confirm_user, new_notification

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

        social = json.loads(data.pop('services')[0])
        data.update(social)

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

        if 'latitude' in data.keys() and 'longitude' in data.keys():
            storage.location = Point(float(data['latitude']), float(data['longitude']), srid=4326)
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
            kwargs['partial'] = True
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def put(self, req, *args, **kwargs):
        storages = Storage.objects.filter(id=self.kwargs['pk'])
        if not storages.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        storage = storages.first()
        if req.user != storage.company_owner.owner:
            return Response('You have no permissions for this Storage', status=status.HTTP_403_FORBIDDEN)

        data = req.data.copy()
        if 'metro' in data.keys():
            storages = Storage.objects.filter(pk=kwargs['pk'])
            if not storages.exists():
                return Response('Error: Storage with this id doesn\'t exist', status=status.HTTP_404_NOT_FOUND)
            storage = storages.first()
            metro_data = json.loads(data['metro'])

            storage.metro.clear()
            for station in metro_data:
                new_station = station_get_or_create(station)
                storage.metro.add(new_station)
            storage.save()

        return super().put(req, *args, **kwargs)


class FilterStoragesView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]
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


class ManagerRegisterView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerRegistrationSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser,)

    def post(self, req, **kwargs):
        storages = Storage.objects.filter(id=self.kwargs['pk'])
        if not storages.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        storage = storages.first()

        if req.user != storage.company_owner.owner:
            return Response('You have no permissions for this Storage', status=status.HTTP_403_FORBIDDEN)

        if not confirm_user(int(req.data.get('telegram_id')), storage.id):
            return Response('Error: Something wrong, check your data and try again', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        manager_serializer = self.serializer_class(data=req.data)
        if not manager_serializer.is_valid():
            return Response(manager_serializer.errors, status=status.HTTP_200_OK)
        manager = manager_serializer.save()

        manager.storage = storage.id
        manager.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, req, **kwargs):
        storage = Storage.objects.filter(id=self.kwargs['pk'])
        if not storage.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        managers = ManagerSerializer(data=storage.managers, many=True)
        return Response(managers.data, status=status.HTTP_200_OK)


class ManagerView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser,)

    def get(self, req, **kwargs):
        managers = Manager.objects.filter(telegram_id=req.data['telegram_id'])
        if not managers.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        manager = managers.first()

        manager_data = self.serializer_class(manager)
        return Response(manager_data.data, status=status.HTTP_200_OK)

    def delete(self, req, *args, **kwargs):

        managers = Manager.objects.filter(telegram_id=req.data['telegram_id'])
        if not managers.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        manager = managers.first()
        manager.delete()
        return Response(status=status.HTTP_200_OK)


class GetAllFeedbackView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Storage.objects.all()
    serializer_class = StorageFeedbackSerializer
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        storage = Storage.objects.filter(id=self.kwargs['pk'])
        if not storage.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = storage.feedbacks
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllStoragesMapView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Storage.objects.all()
    serializer_class = StorageCoordinatesSerializer
    renderer_classes = [JSONRenderer]
    filterset_class = StorageFilter

    def get(self, req, **kwargs):
        user_location = Point(float(req.GET.get('latitude')), float(req.GET.get('longitude')), srid=4326)
        queryset = self.filter_queryset(self.get_queryset()).annotate(distance=Distance('location', user_location)).order_by('distance')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def distance_to_decimal_degrees(distance, latitude):
    """
    Source of formulae information:
        1. https://en.wikipedia.org/wiki/Decimal_degrees
        2. http://www.movable-type.co.uk/scripts/latlong.html
    :param distance: an instance of `from django.contrib.gis.measure.Distance`
    :param latitude: y - coordinate of a point/location
    """
    lat_radians = latitude * (math.pi / 180)
    # 1 longitudinal degree at the equator equal 111,319.5m equiv to 111.32km
    return distance.m / (111_319.5 * math.cos(lat_radians))


class GetNearbyStoragesMap(ListAPIView):
    queryset = Storage.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]
    serializer_class = StorageCoordinatesSerializer
    filterset_class = StorageFilter

    def get(self, req, **kwargs):
        user_location = Point(float(req.GET.get('latitude')), float(req.GET.get('longitude')), srid=4326)
        queryset = self.filter_queryset(self.get_queryset()).annotate(distance=Distance('location', user_location)).filter(distance__lte=distance_to_decimal_degrees(D(m=10000), user_location.y)).order_by('distance')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MoveLngLatToLocation(APIView):
    queryset = Storage.objects.all()
    permission_classes = (AllowAny, )

    def get(self, req, **kwargs):
        for storage in self.queryset.all():
            storage.location = Point(float(storage.latitude), float(storage.longtude), srid=4326)
            storage.save()
        return Response(status.HTTP_200_OK)

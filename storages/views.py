from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from .serializers import StorageRegistrationSerializer, SingleStorageSerializer
from .models import Storage

from .models import Storage, ACCESS_TYPE, SURVEILLANCE_TYPE, TEMPERATURE_TYPE
from .serializers import StorageRegistrationSerializer, StorageSerializer
from images.serializers import ImageSerializer
from images.models import ImageAlbum

from django.db.models import Q


class StorageRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StorageRegistrationSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser,)

    def post(self, req, **kwargs):
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
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(storage.id, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class StorageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]
    queryset = Storage.objects.all()


class FilterStoragesView(APIView):
    permission_classes = (AllowAny,)
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    renderer_classes = [JSONRenderer]

    def get(self, req):
        square_min = int(req.GET.get('square_min', 0))
        square_max = int(req.GET.get('square_max', 10000))
        price_min = int(req.GET.get('price_min', 0))
        price_max = int(req.GET.get('price_max', 100000))
        access = req.GET.get('access', ACCESS_TYPE)
        work_hours_start = req.GET.get('work_hours_start', '00:00:00')
        work_hours_end = req.GET.get('work_hours_end', '23:59:59')
        surveillance = req.GET.get('surveillance', SURVEILLANCE_TYPE)
        climate = req.GET.get('climate', TEMPERATURE_TYPE)
        storages = self.queryset.filter(Q(square__gte=square_min) & Q(square__lte=square_max) &
                                        Q(price__gte=price_min) & Q(price__lte=price_max) &
                                        Q(climate__in=climate) & Q(access__in=access))
        # storages = self.queryset.filter(Q(square__gte=square_min) & Q(square__lte=square_max) &
        #                                 Q(price__gte=price_min) & Q(price__lte=price_max) &
        #                                 Q(access__in=access) & Q(climate__in=climate) &
        #                                 Q(work_hours_start__gte=work_hours_start) & Q(work_hours_end__lte=work_hours_end) &
        #                                 Q(surveillance__in=surveillance))
        # storages = self.queryset.filter(climate__in=climate)
        data = self.serializer_class(storages, many=True).data
        return Response(data, status=status.HTTP_200_OK)

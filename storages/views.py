# from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import decorators

from rest_framework.permissions import AllowAny

from .models import Storage
from .serializers import StorageRegistrationSerializer, StorageSerializer


@decorators.api_view(["POST", "GET", "DELETE"])
@decorators.permission_classes([AllowAny])
def storage(req):
    if req.method == 'POST':
        serializer = StorageRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        storages = serializer.save()
        user = req.user
        storages.owner = user.company
        storages.save()
        return Response(storages.id, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})
    elif req.method == 'GET':
        storage_id = req.GET.get('storage_id')
        storages = Storage.objects.filter(id=storage_id).first()
        if storages is None:
            return Response("Storage with this id does\'t exist", status.HTTP_404_NOT_FOUND)
        data = StorageSerializer(storages).data
        return Response(data, status.HTTP_200_OK)
    elif req.method == 'DELETE':
        storage_id = req.GET.get('storage_id')
        storages = Storage.objects.filter(id=storage_id).first()
        if storages is None:
            return Response("Storage with this id does\'t exist", status.HTTP_404_NOT_FOUND)
        storages.remove()
        return Response(status=status.HTTP_200_OK)
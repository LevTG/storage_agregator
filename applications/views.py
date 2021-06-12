from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ApplicationRegistrationSerializer, ApplicationSerializer
from .models import Application
from storages.models import Storage


@api_view(["POST"])
def my_application(req):
    if req.method == 'POST':
        data = req.data.copy()
        storage_id = int(data.pop('storage_id')[0])
        storages = Storage.objects.filter(id=storage_id)
        if storages.exists():
            storage = storages[0]
            data['storage'] = storage
            serializer = ApplicationRegistrationSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_200_OK)
            application = serializer.save()
            return Response(application.id, status=status.HTTP_201_CREATED)
        else:
            return Response("Storage with this id does\'t exist", status.HTTP_404_NOT_FOUND)
    # elif req.method == 'DELETE':


@api_view(['GET'])
def get_all_applications(req):
    user = req.user
    applications = user.applications()
    data = ApplicationSerializer(applications, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def change_status(req):
    new_status = req.post.get('new_status')
    application_id = req.post.get('application_id')
    application = Application.objects.filter(id=application_id)
    if application.exists():
        application.update(status=new_status)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response("Application with this id does\'t exist", status.HTTP_404_NOT_FOUND)

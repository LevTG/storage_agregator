from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ApplicationRegistrationSerializer, ApplicationSerializer
from .models import Application
from storages.models import Storage


#import os, sys
#sys.path.append('/home/backy/tgbot')
from tgbot.telegram_bot import new_notification, mailing


class ApplicationRegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ApplicationRegistrationSerializer

    def post(self, req):
        data = req.data.copy()
        storage_id = data.pop('storage_id')[0]
        storages = Storage.objects.filter(id=storage_id)
        if storages.exists():
            storage = storages[0]
            user = storage.company_owner.owner
            data['storage'] = storage.id
            data['recipient'] = user.id
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_200_OK)
            application = serializer.save()
            
            managers = storage.managers
            mailing(managers, 'Вам поступила новая заявка')
            return Response(application.id, status=status.HTTP_201_CREATED)
        else:
            return Response("Storage with this id does\'t exist", status.HTTP_404_NOT_FOUND)


class SingleApplicationView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ApplicationSerializer



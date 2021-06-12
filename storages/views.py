from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated
from .serializers import StorageRegistrationSerializer, SingleStorageSerializer


class StorageRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StorageRegistrationSerializer


class StorageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SingleStorageSerializer

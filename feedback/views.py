from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import StorageFeedback
from .serializers import StorageFeedbackRegisterSerializer, StorageFeedbackSerializer
from storages.models import Storage


class FeedbackRegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StorageFeedbackRegisterSerializer

    def post(self, req, *args, **kwargs):
        data = req.data.copy()
        storage_id = data.pop('storage_id')[0]
        storages = Storage.objects.filter(id=storage_id)
        if storages.exists():
            storage = storages[0]
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_200_OK)
            feedback = serializer.save()
            feedback.storage = storage
            feedback.author = req.user
            feedback.save()
            return Response(feedback.id, status=status.HTTP_201_CREATED)
        else:
            return Response("Storage with this id does\'t exist", status.HTTP_404_NOT_FOUND)


class SingleFeedbackView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StorageFeedbackSerializer
    queryset = StorageFeedback.objects.all()

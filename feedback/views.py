from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import StorageFeedback, Answer
from .serializers import *
from storages.models import Storage


class FeedbackRegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StorageFeedbackRegistrationSerializer

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


class FeedbackView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StorageFeedbackSerializer
    queryset = StorageFeedback.objects.all()


class AnswerRegistrationView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AnswerRegistrationSerializer

    def post(self, req, *args, **kwargs):
        data = req.data.copy()
        feedback_id = data.pop('feedback_id')[0]
        feedbacks = StorageFeedback.objects.filter(id=feedback_id)
        if feedbacks.exists():
            feedback = feedbacks[0]
            answer = Answer.objects.create(text=data['text'], feedback=feedback, user=req.user)
            answer.save()
            return Response(answer.id, status=status.HTTP_201_CREATED)
        else:
            return Response("Feedback with this id does\'t exist", status.HTTP_404_NOT_FOUND)


class AnswerView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class ReviewRegisterView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ReviewRegistrationSerializer

    def post(self, req, *args, **kwargs):
        data = req.data.copy()
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        review = serializer.save()
        review.save()
        return Response(review.id, status=status.HTTP_201_CREATED)

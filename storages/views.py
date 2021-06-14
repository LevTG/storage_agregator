from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .serializers import StorageRegistrationSerializer, SingleStorageSerializer
from company.models import Company


class StorageRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StorageRegistrationSerializer
    renderer_classes = [JSONRenderer]

    def post(self, req):
        data = req.data.copy()
        company = Company.objects.filter(id=req.data['company_id'])
        if company.exists():
            data['company_owner'] = company.first().id
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_200_OK)
            storage = serializer.save()
            return Response(storage.id, status=status.HTTP_200_OK)
        return Response('Error: company with this id doesn\'t exist', status=status.HTTP_200_OK)

class StorageView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SingleStorageSerializer
    renderer_classes = [JSONRenderer]

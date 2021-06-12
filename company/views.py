from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Company
from .serializers import SingleCompanySerializer, CompanySerializer
from storages.serializers import StorageSerializer


class CompanyRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = SingleCompanySerializer


class SingleCompanyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, AllowAny)
    queryset = Company.objects.all()
    serializer_class = SingleCompanySerializer


class GetAllStorages(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = Company.objects.get(id=company_id)
            storages = company.storage_set
            data = StorageSerializer(storages, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
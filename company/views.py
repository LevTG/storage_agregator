from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Company
from .serializers import SingleCompanySerializer, CompanySerializer
from storages.serializers import StorageSerializer


class CompanyRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = SingleCompanySerializer
    renderer_classes = [JSONRenderer]


class SingleCompanyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = self.queryset.get(id=company_id)
            data = self.serializer_class(company).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)


class GetAllStorages(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]
    queryset = Company.objects.all()
    serializer_class = StorageSerializer

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = self.queryset.get(id=company_id)
            storages = company.storage_set

            serializer_context = {
                'request': req,
            }

            data = self.serializer_class(storages, many=True, context=serializer_context).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)
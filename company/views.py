import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from .models import Company
from images.models import Image
from .serializers import SingleCompanySerializer, CompanySerializer
from storages.serializers import StorageSerializer
from images.serializers import ImageSerializer, ImageRegisterSerializer


class CompanyRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = SingleCompanySerializer
    renderer_classes = [JSONRenderer]


class SingleCompanyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
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


class LogoView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    renderer_classes = [JSONRenderer]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = self.queryset.get(id=company_id)
            logo = company.logo
            data = ImageSerializer(logo).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)

    def put(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = self.queryset.get(id=company_id)

            if company.logo is not None:
                logo_id = company.logo_id

                old_logo = Image.objects.get(id=logo_id)
                old_logo.delete()

            new_logo = req.data['logo']
            image_serializer = ImageRegisterSerializer(data={'image': new_logo, 
                                                     'name': '{}'.format(uuid.uuid4), 
                                                     'category': 'c'})

            if not image_serializer.is_valid():
                return Response(image_serializer.errors, status=status.HTTP_200_OK)
            logo = image_serializer.save()
            company.logo = logo
            company.save()

            return Response(self.serializer_class(company).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)

    def delete(self, req, **kwargs):
        try:
            company_id = self.kwargs['id']
            company = self.queryset.get(id=company_id)

            logo_id = company.logo_id

            old_logo = Image.objects.get(id=logo_id)
            old_logo.delete()

            return Response(self.serializer_class(company).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)

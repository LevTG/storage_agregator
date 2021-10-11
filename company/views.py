import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from .models import Company
from images.models import Image
from .serializers import CompanyRegistrationSerializer, CompanySerializer
from storages.serializers import StorageSerializer
from storages.filters import StorageCommonFilter
from images.serializers import ImageSerializer, ImageRegisterSerializer


class CompanyRegisterView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanyRegistrationSerializer
    renderer_classes = [JSONRenderer]


class SingleCompanyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['pk']
            company = self.queryset.get(id=company_id)
            data = self.serializer_class(company).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)


class GetAllCompanies(ListAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = [JSONRenderer]

    def get(self, req, **kwargs):
        companies = Company.objects.filter(status='a').values_list('name', flat=True).order_by('name').distinct()
        data = {'companies': companies}
        return Response(data, status=status.HTTP_200_OK)


class GetAllStorages(ListAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = [JSONRenderer]
    queryset = Company.objects.all()
    serializer_class = StorageSerializer
    filterset_class = StorageCommonFilter

    def get(self, req, **kwargs):
        try:
            company_id = self.kwargs['pk']
            company = self.queryset.get(id=company_id)
            storages = self.filter_queryset(company.storage_set)

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
            company_id = self.kwargs['pk']
            company = self.queryset.get(id=company_id)
            logo = company.logo
            data = ImageSerializer(logo).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)

    def put(self, req, **kwargs):
        try:
            company_id = self.kwargs['pk']
            company = self.queryset.get(id=company_id)

            if req.user != company.owner:
                return Response('You have no permissions for this Company', status=status.HTTP_403_FORBIDDEN)

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
            company_id = self.kwargs['pk']
            company = self.queryset.get(id=company_id)

            if req.user != company.owner:
                return Response('You have no permissions for this Company', status=status.HTTP_403_FORBIDDEN)


            logo_id = company.logo_id

            old_logo = Image.objects.get(id=logo_id)
            old_logo.delete()

            return Response(self.serializer_class(company).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_404_NOT_FOUND)

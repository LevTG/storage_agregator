# from django.http import HttpResponse
import json
import os
import uuid

import sendgrid

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

# from rest_framework_jwt.settings import api_settings
# from rest_framework_jwt.utils import jwt_create_payload as jwt_payload_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_encode_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_decode_handler
from rest_framework_jwt.views import VerifyJSONWebTokenView, RefreshJSONWebTokenView
from .serializers import ProfileRegistrationSerializer, ProfileLoginSerializer, ProfileSerializer, ChangePasswordSerializer, ProfileUpdateSerializer
from company.serializers import CompanyRegistrationSerializer, CompanySerializer
from applications.serializers import ApplicationSerializer
from applications.models import Application, APPLICATION_STATUS
from images.serializers import ImageRegisterSerializer
from storages.serializers import StorageSerializer
from storages.models import Storage


User = get_user_model()


class UserRegistrationView(CreateAPIView):
    serializer_class = ProfileRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, req, **kwargs):
        serializer = ProfileRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        user = serializer.save()
        res = {
            'username': user.username
        }
        try:
            company_data = {}
            company_data['name'] = req.data.get('company_name', user.username)
            company_data['owner'] = user.id
            company = CompanyRegistrationSerializer(data=company_data)

            user.is_private = (company_data['name'] == user.username)
            user.is_owner = (company_data['name'] == user.username)

            if not company.is_valid():
                user.delete()
                return Response(company.errors, status=status.HTTP_200_OK)
            company = company.save()

            image = req.data.get('logo', None)
            if image is not None:
                form_data = {'image': image, 'category': 'c', 'name': '{}'.format(uuid.uuid4)}
                image_serializer = ImageRegisterSerializer(data=form_data)

                if not image_serializer.is_valid():
                    company.delete()
                    user.delete()
                    return Response(image_serializer.errors, status=status.HTTP_200_OK)
                image = image_serializer.save()
                company.logo = image
                company.save()
            else:
                res['logo'] = 'No logo'
            res['company_id'] = company.id
        except Exception as e:
            user.delete()
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class FetchUserView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = ProfileSerializer


class GetAllCompaniesView(APIView):
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, req):
        user = req.user
        companies = user.companies
        serializer = self.serializer_class(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileLoginSerializer

    def post(self, req):
        serializer = self.serializer_class(data=req.data)
        if not serializer.is_valid():
            serializer.is_valid()
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        res = {
            'username': serializer.data['username'],
            'token': str(serializer.data['token'])
        }
        return Response(res, status=status.HTTP_200_OK)


class UpdateProfileView(UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'username'


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    lookup_field = 'username'


class RefreshTokenView(RefreshJSONWebTokenView):
    def post(self, req, **kwargs):
        serializer = RefreshJSONWebTokenView.serializer_class(data=req.data)
        if serializer.is_valid():
            res = Response(serializer.data, status=status.HTTP_200_OK)
        else:
            res = Response(serializer.errors, status=status.HTTP_200_OK)
        return res


class VerifyTokenView(VerifyJSONWebTokenView):
    def post(self, req, **kwargs):
        serializer = VerifyJSONWebTokenView.serializer_class(data=req.data)
        if serializer.is_valid():
            res = Response(serializer.data, status=status.HTTP_200_OK)
        else:
            res = Response('Error: decoding token', status=status.HTTP_200_OK)
        return res

# class ProfileLogoutView(RetrieveAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, req):
#         try:
#             token = req.data["token"]
#             token.blacklist()
#
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(str(e.__class__) + ' ' + str(e),status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProfileLogoutAllView(RetrieveAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, req):
#         tokens = OutstandingToken.objects.filter(user_id=req.user.id)
#         for token in tokens:
#             t, _ = BlacklistedToken.objects.get_or_create(token=token)
#         return Response(status=status.HTTP_205_RESET_CONTENT)


class GetAllApplicationsView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ApplicationSerializer

    def get(self, req):
        user = req.user
        if user.is_staff:
            applications = Application.objects.filter(status='m')
        else:
            applications = user.application_set.filter(status='a')
        data = self.serializer_class(applications, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class GetAllStoragesView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = StorageSerializer

    def get(self, req, **kwargs):
        user = req.user
        if user.is_staff:
            storages = Storage.objects.filter(status='m')
        else:
            storages = user.storages
        data = self.serializer_class(storages, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RestorePasswordView(APIView):
    permission_classes = (AllowAny, )

    def post(self, req, **kwargs):
        email = req.data.get('email')
        qs = User.objects.filter(email=email)

        if len(qs) > 0:
            user = qs[0]
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save(update_fields=['password'])

            sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

            letter = {"personalizations": [{
                            "to": [
                                    {
                                        "email": email
                                    }
                                ],
                      }],
                      "subject": "New password",
                      "from": {
                            "email": 'administrator@findsklad.ru'
                      },
                      "content": [
                      {
                          "type": "text/plain",
                          "value": "Here is your new password,\n {}".format(password)
                      }],
            }
            try:
                response = sg.client.mail.send.post(request_body=letter)
            except Exception as e:
                raise Exception(e.body)
            return Response('Status sent email {}'.format(response.status_code), status=status.HTTP_200_OK)
        return Response('Error: User not found', status=status.HTTP_404_NOT_FOUND)

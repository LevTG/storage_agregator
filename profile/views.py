# from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

# from rest_framework_jwt.settings import api_settings
# from rest_framework_jwt.utils import jwt_create_payload as jwt_payload_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_encode_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_decode_handler
from rest_framework_jwt.views import VerifyJSONWebTokenView, RefreshJSONWebTokenView
from .serializers import ProfileRegistrationSerializer, ProfileLoginSerializer, ProfileSerializer, ChangePasswordSerializer, ProfileUpdateSerializer
from company.serializers import SingleCompanySerializer, CompanySerializer
from applications.serializers import ApplicationSerializer
from images.serializers import ImageSerializer


User = get_user_model()


class UserRegistrationView(CreateAPIView):
    serializer_class = ProfileRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, req):
        # return Response(req.data['profile'])
        serializer = ProfileRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        user = serializer.save()
        res = {
            'username': user.username
        }
        try:
            if 'name' in req.data['company'].keys():
                data = req.data['company'].copy()
                data['owner'] = user.id
                company = SingleCompanySerializer(data=data)
                user.is_private = False
                user.is_owner = True
                if not company.is_valid():
                    return Response(company.errors, status=status.HTTP_200_OK)
            else:
                data = req.data['company'].copy()
                data['owner'] = user.id
                data['name'] = user.username
                data['is_private'] = True
                company = SingleCompanySerializer(data=data)
                user.is_owner = True
                user.save()
                if not company.is_valid():
                    return Response(company.errors, status=status.HTTP_200_OK)
            company = company.save()
            image = req.FILES.get('logo', None)
            if image is not None:
                form_data = {}
                form_data['image'] = image
                form_data['name'] = 'company'

                image_serializer = ImageSerializer(data=form_data)

                if not image_serializer.is_valid():
                    return Response(image_serializer.errors, status=status.HTTP_200_OK)
                image = image_serializer.save()
                company.logo = image.id
            res['company_id'] = company.id
        except Exception as e:
            user.delete()
            return Response(str(e.__class__) + ' ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})


class FetchUserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
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
    def post(self, req):
        serializer = RefreshJSONWebTokenView.serializer_class(data=req.data)
        if serializer.is_valid():
            res = Response(serializer.data, status=status.HTTP_200_OK)
        else:
            res = Response(serializer.errors, status=status.HTTP_200_OK)
        return res


class VerifyTokenView(VerifyJSONWebTokenView):
    def post(self, req):
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

    def get(self, req):
        user = req.user
        applications = user.application_set
        data = ApplicationSerializer(applications, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class GetAllStoragesView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, req):
        user = req.user
        applications = user.storages
        data = ApplicationSerializer(applications, many=True).data
        return Response(data, status=status.HTTP_200_OK)

# from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

# from rest_framework_jwt.settings import api_settings
# from rest_framework_jwt.utils import jwt_create_payload as jwt_payload_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_encode_handler
# from rest_framework_jwt.utils import jwt_encode_payload as jwt_decode_handler

from .serializers import ProfileRegistrationSerializer, ProfileLoginSerializer, ProfileSerializer, ChangePasswordSerializer, ProfileUpdateSerializer
from company.serializers import SingleCompanySerializer, CompanySerializer


User = get_user_model()


class UserRegistrationView(CreateAPIView):
    serializer_class = ProfileRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, req):
        # return Response(req.data['profile'])
        serializer = ProfileRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        res = {
            'username': user.username
        }
        try:
            if 'company' in req.data.keys():
                company = SingleCompanySerializer(data={'name': req.data['company_name'], 'owner': user.id})
                user.is_private = False
                user.is_owner = True
            else:
                company = SingleCompanySerializer(data={'name': user.username, 'is_private': True, 'owner': user.id})
                user.is_owner = True
                user.save()
                if not company.is_valid():
                    return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)
            company = company.save()
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


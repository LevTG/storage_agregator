# from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer, UserSerializer, ChangePasswordSerializer, UpdateUserSerializer
from company.serializers import CompanyRegistrationSerializer


User = get_user_model()


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def registration(req):
    if req.method == 'POST':
        serializer = RegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        try:
            if 'company_name' in req.data.keys():
                company = CompanyRegistrationSerializer(data={'name': req.data['company_name'], 'owner': user.pk})
                user.is_private = False
                user.is_owner = False
            else:
                company = CompanyRegistrationSerializer(data={'name': user.username, 'is_private': True,  'owner': user.pk})
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
    elif req.method == 'GET':
        user = req.user
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(self, req):
    try:
        refresh_token = req.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_all(self, req):
    tokens = OutstandingToken.objects.filter(user_id=req.user.id)
    for token in tokens:
        t, _ = BlacklistedToken.objects.get_or_create(token=token)
    return Response(status=status.HTTP_205_RESET_CONTENT)


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

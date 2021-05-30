from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer

from django.contrib.auth import get_user_model
from rest_framework import decorators
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@decorators.api_view(["POST", "GET"])
@decorators.permission_classes([AllowAny])
def registration(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(res, status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})
    else:
        return Response({'data': 'Success'})
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import FAQRegistrationSerializer, FAQSerializer
from .models import Faq


@api_view(["POST", "GET"])
# @permission_classes([AllowAny])
def questions(req):
    if req.method == 'POST':
        serializer = FAQRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    elif req.method == 'GET':
        count = req.GET.get('count')
        if count is not None:
            questions_local = Faq.objects.all()[:int(count)]
        else:
            questions_local = Faq.objects.all()
        data = FAQSerializer(questions_local).data
        return Response(data, status.HTTP_200_OK)




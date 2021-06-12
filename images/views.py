from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def upload_image(req):
    image = req.FILES
    return Response()

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Company
from .serializers import CompanyRegistrationSerializer, CompanySerializer


# class AddView(APIView):
#

@login_required
@api_view(["POST"])
# @permission_classes([AllowAny])
def companies(req):
    if req.method == 'POST':
        if 'company_id' in req.data.keys() and 'changes' in req.data.keys():
            company = Company.objects.filter(id='company_id')
            if company.exists():
                data = req.data
                company_id = data['company_id']
                company.update(**data['changes'])
                company.save()
                return Response(company_id, status=status.HTTP_200_OK)
            else:
                return Response("Company with this id does\'t exist", status.HTTP_404_NOT_FOUND)

        serializer = CompanyRegistrationSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)
        company = serializer.save()

        user = req.user
        company.owner(user)
        company.save()
        return Response(status=status.HTTP_201_CREATED)
    elif req.method == 'GET':
        company = req.user.company
        if company.exists():
            data = CompanySerializer(company).data
            return Response(data, status.HTTP_200_OK)
        else:
            return Response("This user haven\'t company yet", status.HTTP_404_NOT_FOUND)
    elif req.method == 'DELETE':
        company = req.user.company
        if company.exists():
            company.first().remove()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("This user haven\'t company yet", status.HTTP_404_NOT_FOUND)


class CompanyView(APIView):

    def get(self, req, **kwargs):
        try:
            pk = self.kwargs['pk']
            company = Company.objects.get(pk=pk)
            data = CompanySerializer(company).data
            return JsonResponse(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

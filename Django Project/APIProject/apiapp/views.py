from django.shortcuts import render
from .models import userInfo
from rest_framework.decorators import api_view
from .serializers import userSerialziers
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    userdata=userInfo.objects.all()
    userserial=userSerialziers(userdata,many=True)
    return Response(userserial.data)







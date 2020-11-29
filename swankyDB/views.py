from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

from datetime import datetime, timedelta


# Saves a licenses' information
class saveLicense(generics.CreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseCreateSerializer


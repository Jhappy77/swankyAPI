from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

from datetime import datetime, timedelta


## Don't do anything with the User Model just yet. Django has some predefined user
## stuff that we should probably use instead, I will look into it tomorrow morning

# Saves a licenses' information
# (This is a template view so we don't have to do much work. More complex views will require more work)
class saveLicense(generics.CreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


# If you want to make views, you can see the views I made at https://github.com/Jhappy77/swagadellicAPI/tree/main/swagDB in views.py for inspiration


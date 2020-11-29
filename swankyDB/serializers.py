from rest_framework import serializers
from .models import *

class LicenseCreateSerializer:
    class Meta:
        model = License
        fields = ("license_id", "type", "renter")
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User 


################ USERS ##############

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("ssn", "name")

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("person", "username")

class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renter
        fields = ("client", "admin_manager")

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("client", "admin_id")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")

class Admin_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_User
        fields = ("username", "admin_id")



########## VEHICLES & MANUFACTURERS #############

class Vehicle_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Type
        fields = ("id", "model", "manufacturer_name", "license_type", "default_img")

class Vehicle_InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Instance
        fields = ("id", "serial_no", "type_id", "preview_image_url")

class SpacecraftSerializerNoNest(serializers.ModelSerializer):
    class Meta:
        model = Spacecraft
        fields = ("id", "max_weight", "max_thrust", "fuel_type", "vehicle_type")

class SpacecraftSerializer(serializers.ModelSerializer):
    vehicle_type = Vehicle_TypeSerializer("vehicle_type")
    class Meta:
        model = Spacecraft
        fields = ("id", "max_weight", "max_thrust", "fuel_type", "vehicle_type")

class Land_VehicleSerializerNoNest(serializers.ModelSerializer):
    class Meta:
        model = Land_Vehicle
        fields = ("id", "vehicle_type", "max_speed", "fuel_type", "horsepower")

class Land_VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = Vehicle_TypeSerializer("vehicle_type")
    class Meta:
        model = Land_Vehicle
        fields = ("id", "vehicle_type", "max_speed", "fuel_type", "horsepower")

class WatercraftSerializerNoNest(serializers.ModelSerializer):
    class Meta:
        model = Watercraft
        fields = ("id", "vehicle_type", "max_speed", "length", "capacity")

class WatercraftSerializer(serializers.ModelSerializer):
    vehicle_type = Vehicle_TypeSerializer("vehicle_type")
    class Meta:
        model = Watercraft
        fields = ("id", "vehicle_type", "max_speed", "length", "capacity")

class AircraftSerializerNoNest(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ("id", "vehicle_type", "engine_count", "takeoff_speed", "seat_count")

class AircraftSerializer(serializers.ModelSerializer):
    vehicle_type = Vehicle_TypeSerializer("vehicle_type")
    class Meta:
        model = Aircraft
        fields = ("id", "vehicle_type", "engine_count", "takeoff_speed", "seat_count")

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("id", "name", "home_country", "year_founded")



####### RENTING INFO ################


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("contract_no", "money", "start_date", "end_date")

class RentsSerializer(serializers.ModelSerializer):
    theContract = ContractSerializer(many=False, read_only=True)
    class Meta:
        model = Rents
        fields = ("renter", "vehicle", "theContract")

class RentsPostSerializer(serializers.ModelSerializer):
    # theContract = ContractSerializer(many=False, read_only=True)
    class Meta:
        model = Rents
        fields = ("renter", "vehicle", "contract_no")

class Rents_OutSerializer(serializers.ModelSerializer):
    vehicle = Vehicle_InstanceSerializer("vehicle")
    class Meta:
        model = Rents_Out
        fields = ("partner", "vehicle", "daily_rate")


## LICENSE INFO ###############

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ("license_id", "type", "renter")

class License_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = License_Type
        fields = ("type",)

## SPACESHIP PARTS ############
class Made_Spaceship_PartSerializer(serializers.ModelSerializer):
    spacecraft_id = SpacecraftSerializer("spacecraft_id")
    class Meta:
        model = Made_Spaceship_Parts
        fields = ("spacecraft_id", "manufacturer", "part_name")

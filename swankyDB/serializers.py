from rest_framework import serializers
from .models import *

####### These serializers are not finalized!!! ############
# They're just a starting point. Some of them need the fields updated,
# because I made a few changes to the model.
# They all need to be constructed with model serializer, like license serialzier (Elgiz forgot to)
# Finally, you may need to make more complex serializers for specific situations.


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ("license_id", "type", "renter")

class PersonSerializer:
    class Meta:
        model = Person
        fields = ("ssn", "name")

class ClientSerializer:
    class Meta:
        model = Client
        fields = ("ssn", "username")

class RenterSerializer:
    class Meta:
        model = Renter
        fields = ("username", "admin_manager")

class PartnerSerializer:
    class Meta:
        model = Partner
        fields = ("username", "admin_id")

class ContractSerializer:
    class Meta:
        model = Contract
        fields = ("contract_no", "money", "start_date", "end_date")

class ManufacturerSerializer:
    class Meta:
        model = Manufacturer
        fields = ("name", "home_country", "year_founded")

class Rents_OutSerializer:
    class Meta:
        model = Rents_Out
        fields = ("username", "vehicle", "daily_rate")

class Vehicle_InstanceSerializer:
    class Meta:
        model = Vehicle_Instance
        fields = ("serial_no", "type_id", "preview_image_paths")

class SpacecraftSerializer:
    class Meta:
        model = Spacecraft
        fields = ("vehicle_type", "max_weight", "max_thrust", "fuel_type")

class Land_VehicleSerializer:
    class Meta:
        model = Land_Vehicle
        fields = ("vehicle_type", "max_speed", "fuel_type", "horsepower")

class AircraftSerializer:
    class Meta:
        model = Aircraft
        fields = ("vehicle_type", "engine_count", "takeoff_speed", "seat_count")

class Vehicle_TypeSerializer:
    class Meta:
        model = Vehicle_Type
        fields = ("id", "model", "manufacturer_name", "license_type", "default_img")

class UserSerializer:
    class Meta:
        model = User
        fields = ("username", "password", "email")

class Admin_UserSerializer:
    class Meta:
        model = Admin_User
        fields = ("username", "admin_id")

class License_TypeSerializer:
    class Meta:
        model = License_Type
        fields = ("type")

class LicenseSerializer:
    class Meta:
        model = License
        fields = ("renter", "license_id", "type")

class RentsSerializer:
    class Meta:
        model = Rents
        fields = ("username", "vehicle", "daily_rate")
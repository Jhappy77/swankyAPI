from django.db import models
from django.contrib.auth.models import User 

#### USERS #########

# class User(models.Model):
#     username = models.CharField(max_length=30, primary_key=True)
#     password = models.CharField(max_length=30)
#     email = models.CharField(max_length=50)

class Admin_User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=10, primary_key=True)


class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=10, primary_key=True)


class Person(models.Model):
    ssn = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Renter(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_manager = models.ForeignKey(Admin_User, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Partner(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin_User, on_delete=models.SET_NULL, null=True, blank=True, default=None)



###### VEHICLE MODELS ###############

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    home_country = models.CharField(max_length=100)
    year_founded = models.IntegerField()



# The primary key for this model is id. It is auto included and created by Django. 
class Vehicle_Type(models.Model):
    model = models.CharField(max_length=100)
    manufacturer_name = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    license_type = models.ForeignKey('License_Type', on_delete=models.CASCADE)
    default_img = models.URLField(max_length=200, null=True, blank=True, default=None)

## The primary key for this model is id. (Auto-included by Django)
class Vehicle_Instance(models.Model):
    serial_no = models.IntegerField()
    type_id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    preview_image_url = models.URLField(max_length=120, null=True, blank=True, default=None)

    # This forces the combination of type and serial number to be unique
    class Meta:
        unique_together = (("serial_no", "type_id"),)

class Spacecraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_weight = models.IntegerField()
    max_thrust = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)


class Land_Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    horsepower = models.IntegerField()


class Watercraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    length = models.IntegerField()
    capacity = models.CharField(max_length=100)


class Aircraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    engine_count = models.IntegerField()
    takeoff_speed = models.IntegerField()
    seat_count = models.IntegerField()


class Made_Spaceship_Parts(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    spacecraft_id = models.ForeignKey(Spacecraft, on_delete=models.CASCADE)
    part_name = models.CharField(max_length=100)



########## RENTING INFO ###############


class Contract(models.Model):
    contract_no = models.CharField(primary_key=True, max_length=10)
    money = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Rents_Out(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    daily_rate = models.IntegerField()

class Rents(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    contract_no = models.ForeignKey(Contract, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)

class License_Type(models.Model):
    type = models.CharField(max_length=10, primary_key=True)

class License(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    license_id = models.CharField(primary_key=True, max_length=25)
    type = models.ForeignKey(License_Type, on_delete=models.CASCADE)



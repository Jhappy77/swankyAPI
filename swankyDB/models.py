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
    def __str__(self):
        return str(self.username) + " Admin (" + str(self.admin_id) + ")"


class Person(models.Model):
    ssn = models.CharField(max_length=10, primary_key=True) 
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name) + " (SSN = " + str(self.ssn) + ")"

class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return "ClientID: " + str(self.id) + "Username: " + str(self.username) + " (Person= " + str(self.person) + ")"


class Renter(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_manager = models.ForeignKey(
        Admin_User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    def __str__(self):
        return "RenterID: " + str(self.id) + " Client= ( " + str(self.client) +")" + " (Admin Manager = " + str(self.admin_manager) + ")"


class Partner(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(
        Admin_User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    def __str__(self):
        return "PartnerID: " + str(self.id) + "(client = " + str(self.client) + ")" + " (Admin Id = " + str(self.admin_id) + ")"

###### VEHICLE MODELS ###############

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    home_country = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    def __str__(self):
        return str(self.id) + str(self.name) + " (Home Country = " + str(self.home_country) + ")"



# The primary key for this model is id. It is auto included and created by Django. 
class Vehicle_Type(models.Model):
    model = models.CharField(max_length=100)
    manufacturer_name = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    license_type = models.ForeignKey('License_Type', on_delete=models.CASCADE)
    default_img = models.URLField(
        max_length=200, null=True, blank=True, default=None)
    def __str__(self):
        return str(self.id) + str(self.model) + " (Manufacturer = " + str(self.manufacturer_name) + ")"


# The primary key for this model is id. (Auto-included by Django)
class Vehicle_Instance(models.Model):
    serial_no = models.IntegerField()
    type_id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    preview_image_url = models.URLField(
        max_length=120, null=True, blank=True, default=None)
    def __str__(self):
        return str(self.id) +str(self.type_id) + " (Serial no = " + str(self.serial_no) + ")"
        # This forces the combination of type and serial number to be unique
    class Meta:
        unique_together = (("serial_no", "type_id"),)


class Spacecraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_weight = models.IntegerField()
    max_thrust = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id) + str(self.vehicle_type) + " (Fuel type = " + str(self.fuel_type) + ")"


class Land_Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    def __str__(self):
        return str(self.id) +str(self.vehicle_type) + " (Horsepower = " + str(self.horsepower) + ")"


class Watercraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    length = models.IntegerField()
    capacity = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id) +str(self.vehicle_type) + " (Capacity = " + str(self.capacity) + ")"


class Aircraft(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    engine_count = models.IntegerField()
    takeoff_speed = models.IntegerField()
    seat_count = models.IntegerField()
    def __str__(self):
        return str(self.id) +str(self.vehicle_type) + " (Seat Count = " + str(self.seat_count) + ")"


class Made_Spaceship_Parts(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    spacecraft_id = models.ForeignKey(Spacecraft, on_delete=models.CASCADE)
    part_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id) + str(self.part_name) + " (Manufacturer = " + str(self.manufacturer) + ")"


########## RENTING INFO ###############


class Contract(models.Model):
    contract_no = models.CharField(primary_key=True, max_length=10)
    money = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return str(self.contract_no) + " (Start Date = " + str(self.start_date) + ")" + " (End Date = " + str(self.end_date) + ")"


class Rents_Out(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    daily_rate = models.IntegerField()
    def __str__(self):
        return str(self.id) + str(self.partner) + " (Vehicle = " + str(self.vehicle) + ")" + " (Daily Rate = " + str(self.daily_rate) + ")"


class Rents(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    contract_no = models.ForeignKey(Contract, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + str(self.renter) + " (Contract no = " + str(self.contract_no) + ")" + " (Vehicle = " + str(self.vehicle) + ")"


####### LICENSE MODELS ##########


class License_Type(models.Model):
    type = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return str(self.type)


class License(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    license_id = models.CharField(primary_key=True, max_length=25)
    type = models.ForeignKey(License_Type, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.renter) + " (License Id = " + str(self.license_id) + ")" + " (Type = " + str(self.type) + ")"

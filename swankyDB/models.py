from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

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
    username = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_manager = models.CharField(max_length=10)


class Partner(models.Model):
    username = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=10, primary_key=True)


class License_Type(models.Model):
    type = models.CharField(max_length=10, primary_key=True)


class License(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    license_id = models.CharField(primary_key=True, max_length=25)
    type = models.ForeignKey(License_Type, on_delete=models.CASCADE)


class Contract(models.Model):
    contract_no = models.CharField(primary_key=True, max_length=10)
    money = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    home_country = models.CharField(max_length=100)
    year_founded = models.IntegerField()


class Vehicle_Type(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=100)
    manufacturer_name = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    license_type = models.ForeignKey(License_Type, on_delete=models.CASCADE)
    default_img = models.URLField(max_length=200, null=True, blank=True, default=None)

class Vehicle_Instance(models.Model):
    serial_no = models.IntegerField()
    type_id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    preview_image_paths = models.URLField(max_length=200)

    # This forces the combination of type and serial number to be unique
    class Meta:
        unique_together = (("serial_no", "type_id"),)

class Rents_Out(models.Model):
    username = models.ForeignKey(Partner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    daily_rate = models.IntegerField()

class Rents(models.Model):
    username = models.ForeignKey(Renter, on_delete=models.CASCADE)
    contract_no = models.ForeignKey(Contract, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)


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

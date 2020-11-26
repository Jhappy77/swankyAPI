from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=30, primary_key=True)
    Password = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)


class Admin_User(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Admin_id = models.CharField(max_length=10, primary_key=True)


class Client(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Ssn = models.CharField(max_length=10, primary_key=True)


class Person(models.Model):
    Ssn = models.ForeignKey(Client, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)


class Renter(models.Model):
    Username = models.ForeignKey(Client, on_delete=models.CASCADE)
    Admin_manager = models.CharField(max_length=10)


class Partner(models.Model):
    Username = models.ForeignKey(Client, on_delete=models.CASCADE)
    Admin_id = models.CharField(max_length=10, primary_key=True)


class License_Type(models.Model):
    Type = models.CharField(max_length=10, primary_key=True)


class License_Inst(models.Model):
    Renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    License_id = models.IntegerField(primary_key=True)
    Type = models.ForeignKey(License_Type, on_delete=models.CASCADE)


class Contract(models.Model):
    Contract_no = models.CharField(primary_key=True, max_length=10)
    Money = models.IntegerField()
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()


class Manufacturer(models.Model):
    Name = models.CharField(max_length=100)
    Home_country = models.CharField(max_length=100)
    Year_founded = models.IntegerField()


class Vehicle_Type(models.Model):
    Id = models.IntegerField(primary_key=True)
    Model = models.CharField(max_length=100)
    Manufacturer_name = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    License_type = models.ForeignKey(License_Type, on_delete=models.CASCADE)


class Vehicle_Instance(models.Model):
    Serial_no = models.IntegerField(primary_key=True)
    Type_id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Preview_image_paths = models.CharField()


class Rents_Out(models.Model):
    Username = models.ForeignKey(Partner, on_delete=models.CASCADE)
    Vserial_no = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    Vtype_id = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    Daily_rate = models.IntegerField()


class Rents(models.Model):
    Username = models.ForeignKey(Renter, on_delete=models.CASCADE)
    Contract_no = models.ForeignKey(Contract, on_delete=models.CASCADE)
    Vserial_no = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)
    Vtype_id = models.ForeignKey(Vehicle_Instance, on_delete=models.CASCADE)


class Spacecraft(models.Model):
    Id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Max_weight = models.IntegerField()
    Max_thrust = models.CharField(max_length=100)
    Fuel_type = models.CharField(max_length=100)


class Land_Vehicle(models.Model):
    Id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Max_speed = models.IntegerField()
    Fuel_type = models.CharField(max_length=100)
    Horsepower = models.IntegerField()


class Watercraft(models.Model):
    Id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Max_speed = models.IntegerField()
    Length = models.IntegerField()
    Capacity = models.CharField(max_length=100)


class Aircraft(models.Model):
    Id = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Engine_count = models.IntegerField()
    Takeoff_speed = models.IntegerField()
    Seat_count = models.IntegerField()


class Made_Spaceship_Parts(models.Model):
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    Spacecraft_id = models.ForeignKey(Spacecraft, on_delete=models.CASCADE)
    Part_name = models.CharField(max_length=100)

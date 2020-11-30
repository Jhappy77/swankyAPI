from swankyDB.models import Admin_User, Aircraft, Client, Contract, Land_Vehicle, License, License_Type, Made_Spaceship_Parts, Manufacturer, Partner, Person, Renter, Rents, Rents_Out, Spacecraft, Vehicle_Instance, Vehicle_Type, Watercraft
from django.contrib import admin

# Register your models here.
admin.site.register(Admin_User)
admin.site.register(Client)
admin.site.register(Person)
admin.site.register(Partner)
admin.site.register(Renter)


admin.site.register(Manufacturer)
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_Instance)
admin.site.register(Spacecraft)
admin.site.register(Watercraft)
admin.site.register(Land_Vehicle)
admin.site.register(Aircraft)
admin.site.register(Made_Spaceship_Parts)


admin.site.register(Rents_Out)
admin.site.register(Contract)
admin.site.register(Rents)
admin.site.register(License_Type)
admin.site.register(License)
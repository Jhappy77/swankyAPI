from swankyDB.views import getAircrafts, getAvailableSpacecrafts, getLand_Vehicles, getLicenses, getRentedOutVehicles, getWatercrafts
from django.urls import path 
from . import views 

urlpatterns = [



    ################### LICENSES ########################## 
    
    # For a renter to save a license associated with them
    path('save-license', views.saveLicense.as_view(), name='Save License'),

    # Get all license types. Can be used to create enums for registering licenses.
    path('license-types', views.getAllLicense_Types.as_view(), name='License Types'),

    # Get a license of type specified, if it exists
    # path('get-license-type', views.getLicense_Type.as_view(), name='Get License Type'),
    
    # # Check if a renter is allowed to rent a certain type of vehicle.
    # # Passes a vehicleTypeId, and a renterId. 
    # # Returns true if the renter is allowed, false if they aren't.
    # path('can-rent', name='Can rent'),

    # #Returns all the licenses owned by the specified renter
    path('licenses', views.getLicenses.as_view(), name='licenses'),


    ############### RENTING #####################
    

    path('rentables', views.getRentables.as_view(), name='Vehicles that are being rented out by partners'),


    path('rents', views.getRentedOutVehicles.as_view(), name="Vehicles being rented by a renter"),

    ## In the future, implement
    # # For a partner registering a vehicle to rent.
    # #Should pass a partner, a dailyRate ($), a vehicleTypeId, and a serialNumber (optional: preview image url)
    # #Should create a tuple in the VehicleInstance table with the proper values, then a table
    # #in the rents-out table that refers to the newly registered vehicle.
    # #Pass an 200 Response if the request was okay and the tuples were created
    # #Pass a 400 Response if they weren't created or request was bad
    # path('register-rent', name='Register vehicle to rent out'),
    
    # # For a renter to rent out a vehicle.
    # # Should pass a vehicleInstanceId, startDate, endDate, money, and renter
    # # Should create a contract tuple
    # # Should then make a RENTS tuple for the contract, renter, and vehicle
    # path('rent-vehicle', name='Rent vehicle'),


################### VEHICLES ###########################


    # #Should return all vehicle types.
    # path('vehicle-types', name='Vehicle Types'),

    # #Query the spacecraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, thrust, and manufacturers
    # #use generics.ListAPIView
    path('spacecrafts', views.getAvailableSpacecrafts.as_view(), name='Spacecrafts'),

    # #Query the land vehicle instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, and manufacturers
    # #use generics.ListAPIView
    path('land-vehicles', views.getLand_Vehicles.as_view(), name='Land Vehicles'),

    # #Query the watercraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, capacity and manufacturers
    # #use generics.ListAPIView
    path('watercrafts', views.getWatercrafts.as_view(), name='Watercrafts'),

    
    # #Query the watercraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, capacity and manufacturers
    # #use generics.ListAPIView
    path('aircrafts', views.getAircrafts.as_view(), name='Aircrafts'),
    
]
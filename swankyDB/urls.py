from swankyDB.views import getAvailableSpacecrafts, getLicenses, getVehicleInstances
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
    
    # # For a partner registering a vehicle to rent.
    # #Should pass a partner, a dailyRate ($), a vehicleTypeId, and a serialNumber (optional: preview image url)
    # #Should create a tuple in the VehicleInstance table with the proper values, then a table
    # #in the rents-out table that refers to the newly registered vehicle.
    # #Pass an 200 Response if the request was okay and the tuples were created
    # #Pass a 400 Response if they weren't created or request was bad
    # path('register-rent', name='Register vehicle to rent out'),
    
    # # For a renter to rent out a vehicle.
    # # Should pass a startDate, endDate, money to saveContracts
    path('make-contract', views.saveContract.as_view(), name='Make contract'),
    # # Should pass a vehicleInstanceId and renter to saveRents
    # # Should create a contract tuple
    # # Should then make a RENTS tuple for the contract, renter, and vehicle
    path('rent-vehicle', views.saveRents.as_view(), name='Rent vehicle'),


################### VEHICLES ###########################


    # #Should return all vehicle types.
    # path('vehicle-types', name='Vehicle Types'),


    path('vehicle-instances', views.getVehicleInstances.as_view(), name='Vehicle Instances'),
    # #Query the spacecraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, thrust, and manufacturers
    # #use generics.ListAPIView
    path('spacecrafts', views.getAvailableSpacecrafts.as_view(), name='Spacecrafts'),

    # #Query the land vehicle instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, and manufacturers
    # #use generics.ListAPIView
    # path('land-vehicles', name='Land Vehicles'),

    # #Query the watercraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, capacity and manufacturers
    # #use generics.ListAPIView
    # path('watercrafts', name='Watercrafts'),

    
    # #Query the watercraft instances. You should be able to filter by availabilities by date,
    # #filter by minPrice and maxPrice, max_speed, capacity and manufacturers
    # #use generics.ListAPIView
    # path('aircrafts', name='Aircrafts'),


    # # Add any more you think are necessary. There will be some user stuff, but I can take care of that.
    
]
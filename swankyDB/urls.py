from swankyDB.views import deleteLicense, getAircrafts, getAvailableSpacecrafts, getLand_Vehicles, getLicenses, getRentedOutVehicles, getWatercrafts, updateLicense
from django.urls import path 
from . import views 

urlpatterns = [

    # Generic CRUD URL routes
    # path('generic', GET.as_view(), name='Get     '),
    # path('generic/create', CREATE.as_view(), name='Create      '),
    # path('generic/<int:pk>', UPDATE.as_view(), name='Update      '),
    # path('generic/<int:pk>/delete', DESTROY.as_view(), name='Delete    '),



    ################### LICENSES ########################## 
    
    # Returns all the licenses owned by the specified renter
    path('license', views.getLicenses.as_view(), name='licenses'),
    # For a renter to save a license associated with them
    path('license/create', views.saveLicense.as_view(), name='Save License'),
    #Updates a specified license with information
    path('license/<int:pk>', views.updateLicense.as_view(), name='Update License'),
    # Deletes a license
    path('license/<int:pk>/delete', views.deleteLicense.as_view(), name='Delete License'),

     # License Type CRUD

    # Get all license types. Can be used to create enums for registering licenses.
    path('license-type', views.getAllLicense_Types.as_view(), name='License Types'),

    path('license-type/create', views.saveLicenseType.as_view(), name='Create License Types'),
    path('license-type/<str:pk>', views.updateLicenseType.as_view(), name='Update License Types'),
    path('license-type/<str:pk>/delete', views.deleteLicenseType.as_view(), name='Delete License Types'),


    ############### RENTING #####################
    
    ## Contract CRUD
    path('contract', views.getContract.as_view(), name='Get Contract'),
    path('contract/create', views.saveContract.as_view(), name='Create Contract'),
    path('contract/<str:pk>', views.updateContract.as_view(), name='Update Contract'),
    path('contract/<str:pk>/delete', views.deleteContract.as_view(), name='Delete Contract'),





    path('rentables', views.getRentables.as_view(), name='Vehicles that are being rented out by partners'),

    # path('rentables', GET.as_view(), name='Get     '),
    # path('rentables/create', CREATE.as_view(), name='Create      '),
    # path('rentables/<int:pk>', UPDATE.as_view(), name='Update      '),
    # path('rentables/<int:pk>/delete', DESTROY.as_view(), name='Delete    '),



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
    # # Should pass a startDate, endDate, money to saveContracts
    path('make-contract', views.saveContract.as_view(), name='Make contract'),
    # # Should pass a vehicleInstanceId and renter to saveRents
    # # Should create a contract tuple
    # # Should then make a RENTS tuple for the contract, renter, and vehicle
    path('rent-vehicle', views.saveRents.as_view(), name='Rent vehicle'),


################### VEHICLES ###########################


    # #Should return all vehicle types.
    # path('vehicle-types', name='Vehicle Types'),

    # Spacecraft types
    path('spacecrafts', views.getAvailableSpacecrafts.as_view(), name='Spacecrafts'),

    # Land vehicle types
    path('land-vehicles', views.getLand_Vehicles.as_view(), name='Land Vehicles'),

    # Watercraft types
    path('watercrafts', views.getWatercrafts.as_view(), name='Watercrafts'),

    
    # Aircraft types
    path('aircrafts', views.getAircrafts.as_view(), name='Aircrafts'),



    ############## MANUFACTURING #################


    ## Manufacturers CRUD


    ## Spaceship Part Maker CRUD
    
]
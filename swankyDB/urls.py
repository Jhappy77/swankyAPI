from swankyDB.views import deleteLicense, getAircrafts, getAllLicenses, getAvailableSpacecrafts, getLand_Vehicles, getLicenses, getMyRents, getRentedOutVehicles, getWatercrafts, updateLicense
from django.urls import path 
from . import views 
from .login import login_view, signup_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    ##### LOGIN ##########

    path('login-token', obtain_auth_token, name='API Token'),
    path('signup', signup_view.as_view(), name='Sign up'),

    ########################### USERS ########################## 
    
    # Returns all the clients
    path('clients', views.getAllClients.as_view(), name='Get a list of all the clients'),
    # Returns all the renters
    path('renters', views.getAllRenters.as_view(), name='Get a list of all the renters'),
    # Returns all the partners
    path('partners', views.getAllPartners.as_view(), name='Get a list of all the partners'),
    #For our system, clients renters and partners should not be updated or deleted throught the API, but directly from the admin website.

    
    ################### LICENSES ########################## 
    
    # Returns all the licenses owned by the specified renter
    path('license', views.getLicenses.as_view(), name='licenses'),
    # Returns all licenses
    path('license/all', views.getAllLicenses.as_view(), name='All Licenses'),
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


    ## Rentable CRUD
    path('rentables', views.getRentables.as_view(), name='Vehicles that are being rented out by partners'),
    path('rentables/create', views.saveRentOut.as_view(), name='Create Rentable Vehicle'),
    path('rentables/<int:pk>', views.updateRentable.as_view(), name='Update Rentable Vehicle'),
    path('rentables/<int:pk>/delete', views.deleteRentable.as_view(), name='Delete Rentable Vehicle'),


    ## Rents CRUD
    path('rents', views.getRentedOutVehicles.as_view(), name="Vehicles being rented by a renter"),
    path('rents/create', views.saveRents.as_view(), name='Rent out a vehicle'),
    path('rents/<int:pk>', views.updateRents.as_view(), name='Update rent for a vehicle'),
    path('rents/<int:pk>/delete', views.deleteRents.as_view(), name='Delete vehicle renting'),
    # The vehicles you are renting out
    path('rents/mine', views.getMyRents.as_view(), name='Renters set of rents'),

################### VEHICLES ###########################


    # #Should return all vehicle types.
    # path('vehicle-types', name='Vehicle Types'),

    # Spacecraft types
    path('spacecrafts', views.getAvailableSpacecrafts.as_view(), name='Spacecrafts'),
    path('spacecrafts/create', views.saveSpacecraft.as_view(), name='Create Spacecraft'),
    path('spacecrafts/<int:pk>', views.updateSpacecraft.as_view(), name='Update Spacecraft'),
    path('spacecrafts/<int:pk>/delete', views.deleteSpacecraft.as_view(), name='Delete Spacecraft'),

    # Land vehicle types
    path('land-vehicles', views.getLand_Vehicles.as_view(), name='Land Vehicles'),
    path('land-vehicles/create', views.saveLand_Vehicle.as_view(), name='Create Land Vehicles'),
    path('land-vehicles/<int:pk>', views.updateLand_Vehicle.as_view(), name='Update Land Vehicles'),
    path('land-vehicles/<int:pk>/delete', views.deleteLand_Vehicle.as_view(), name='Delete Land Vehicles'),

    # Watercraft types
    path('watercrafts', views.getWatercrafts.as_view(), name='Watercrafts'),
    path('watercrafts/create', views.saveWatercraft.as_view(), name='Create Watercraft'),
    path('watercrafts/<int:pk>', views.updateWatercraft.as_view(), name='Update Watercraft'),
    path('watercrafts/<int:pk>/delete', views.deleteWatercraft.as_view(), name='Delete Watercraft'),
    
    # Aircraft types
    path('aircrafts', views.getAircrafts.as_view(), name='Aircrafts'),
    path('aircrafts/create', views.saveAircraft.as_view(), name='Create Aircraft'),
    path('aircrafts/<int:pk>', views.updateAircraft.as_view(), name='Update Aircraft'),
    path('aircrafts/<int:pk>/delete', views.deleteAircraft.as_view(), name='Delete Aircraft'),


    ## Vehicle types CRUD
    path('vehicle-type', views.getVehicleTypes.as_view(), name='License Types'),
    path('vehicle-type/create', views.saveVehicleTypes.as_view(), name='Create Vehicle Types'),
    path('vehicle-type/<int:pk>', views.updateVehicleTypes.as_view(), name='Update Vehicle Types'),
    path('vehicle-type/<int:pk>/delete', views.deleteVehicleTypes.as_view(), name='Delete Vehicle Types'),


    ## Vehicle Instance CRUD
    path('vehicle-instance', views.getAllVehicle_Instances.as_view(), name='Vehicle Instances'),
    path('vehicle-instance/create', views.saveVehicleInstance.as_view(), name='Create vehicle instance'),
    path('vehicle-instance/<int:pk>', views.updateVehicleInstance.as_view(), name='Update Vehicle instance'),
    path('vehicle-instance/<int:pk>/delete', views.deleteVehicleInstance.as_view(), name='Delete Vehicle Instance'),


    ############## MANUFACTURING #################

    ## Manufacturers CRUD
    path('manufacturer', views.getManufacturers.as_view(), name='Get Manufacturer'),
    path('manufacturer/create', views.saveManufacturers.as_view(), name='Create Manufacturer'),
    path('manufacturer/<int:pk>', views.updateManufacturers.as_view(), name='Update Manufacturer'),
    path('manufacturer/<int:pk>/delete', views.deleteManufacturers.as_view(), name='Delete Manufacturer'),

    ## Spaceship Part CRUD
    path('spaceship-part', views.getSpaceshipParts.as_view(), name='Get Spaceship Parts'),
    path('spaceship-part/create', views.saveSpaceshipParts.as_view(), name='Create Spaceship Part'),
    path('spaceship-part/<int:pk>', views.updateSpaceshipParts.as_view(), name='Update Spaceship Part'),
    path('spaceship-part/<int:pk>/delete', views.deleteSpaceshipParts.as_view(), name='Delete Spaceship Part'),
    
]



from django.shortcuts import render

# Rest framework imports
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Our files
from .models import *
from .serializers import *
from .permissions import *

    #        ____  __.---""---.__  ____
    #       /####\/              \/####\
    #      (   /\ )              ( /\   )
    #       \____/                \____/
    #     __/                          \__
    #  .-"    .                      .    "-.
    #  |  |   \.._                _../   |  |
    #   \  \    \."-.__________.-"./    /  /
    #     \  \    "--.________.--"    /  /
    #   ___\  \_                    _/  /___
    # ./    )))))                  (((((    \.
    # \                                      /
    #  \           \_          _/           /
    #    \    \____/""-.____.-""\____/    /
    #      \    \                  /    /
    #       \.  .|                |.  ./
    #     ." / |  \              /  | \  ".
    #  ."  /   |   \            /   |   \   ".
    # /.-./.--.|.--.\          /.--.|.--.\.-.|
    # Hippity hoppity, this is our '''intellectual''' property

#TODO: In the future, consider adding authentication
# Put this decorator above every view that we want restricted
from django.contrib.auth.decorators import login_required
# @login_required(login_url=OUR_LOGIN_URL)
# This seems to be more for pages than API endpoints
# For API endpoints:
#https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/


# class saveContract(generics.CreateAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer

# class getContract(generics.ListAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer

# class deleteContract(generics.DestroyAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer

# class updateContract(generics.RetrieveUpdateAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer



######### LICENSES #############

## Licenses
class saveLicense(generics.CreateAPIView):
    permission_classes = [RenterPermission]
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class deleteLicense(generics.DestroyAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class updateLicense(generics.RetrieveUpdateAPIView):
    permission_classes = [RenterPermission]
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class getLicenses(generics.ListAPIView):
    permission_classes = [RenterPermission]
    serializer_class = LicenseSerializer
    def get_queryset(self):
        licenses = License.objects.all()
        try:
            renterID = getRenterID(self.request)
            return licenses.filter(renter=renterID)
        except:
            return License.objects.none()

class getAllLicenses(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = LicenseSerializer
    queryset = License.objects.all()


## License Types
class saveLicenseType(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

class getAllLicense_Types(generics.ListAPIView):
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

class deleteLicenseType(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

class updateLicenseType(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer


############### USERS ##################


## Person

class savePerson(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class searchForPerson(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_name = request.query_params.get('query_name', None)
        if ((query_name is None)):
            return Response({'Error': 'Query must include name as query_name'}, status=status.HTTP_400_BAD_REQUEST)
        person_list = Person.objects.filter(name=query_name)
        if not person_list.exists():
            return Response({'Error': 'No Person with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        results = []
        for x in person_list:
            results.append(PersonSerializer(x).data)
        return Response(results)



## Client

class saveClient(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class getAllClients(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class searchForClient(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_name = request.query_params.get('query_name', None)
        if ((query_name is None)):
            return Response({'Error': 'Query must include name as query_name'}, status=status.HTTP_400_BAD_REQUEST)
        client_list = Client.objects.filter(username=query_name)
        if not client_list.exists():
            return Response({'Error': 'No Client with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        results = []
        for x in client_list:
            results.append(ClientSerializer(x).data)
        return Response(results)



## Renter

class saveRenter(generics.CreateAPIView):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer

class getAllRenters(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer

class searchForRenter(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_name = request.query_params.get('query_name', None)
        if ((query_name is None)):
            return Response({'Error': 'Query must include name as query_name'}, status=status.HTTP_400_BAD_REQUEST)
        renter_list = Renter.objects.filter(username=query_name)
        if not renter_list.exists():
            return Response({'Error': 'No Renter with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        results = []
        for x in renter_list:
            results.append(RenterSerializer(x).data)
        return Response(results)


## Partner

class savePartner(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class getAllPartners(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class searchForPartner(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_name = request.query_params.get('query_name', None)
        if ((query_name is None)):
            return Response({'Error': 'Query must include name as query_name'}, status=status.HTTP_400_BAD_REQUEST)
        partner_list = Partner.objects.filter(username=query_name)
        if not partner_list.exists():
            return Response({'Error': 'No Partner with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        results = []
        for x in partner_list:
            results.append(PartnerSerializer(x).data)
        return Response(results)


###################### RENTING ########################

## Contracts
class saveContract(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class getContract(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class deleteContract(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class updateContract(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class searchForContract(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_num = request.query_params.get('query_num', None)
        if ((query_num is None)):
            return Response({'Error': 'Query must include contract id as query_num'}, status=status.HTTP_400_BAD_REQUEST)
        contract_list = Contract.objects.filter(contract_no=query_num)
        if not contract_list.exists():
            return Response({'Error': 'No Contract with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        return Response(PartnerSerializer(contract_list[0]).data)




## Rents

class saveRents(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer

class deleteRents(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer

class updateRents(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer
    
# Vehicles that are in the RENTS table (Can filter by renter)
class getRentedOutVehicles(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RentsSerializer
    def get_queryset(self):
        queryset = Rents.objects.all().select_related('vehicle')
        #TODO: In the future, add filter by dates?
        # minPrice = self.request.query_params.get('minPrice', None)
        # if minPrice is not None:
        #     queryset = queryset.filter(daily_rate__gte=minPrice)
        # maxPrice = self.request.query_params.get('maxPrice', None)
        # if maxPrice is not None:
        #     queryset = queryset.filter(daily_rate__lte=maxPrice)
        renter = self.request.query_params.get('renter', None)
        if renter is not None:
            queryset = queryset.filter(renter=renter)
        return queryset

class getAllRentedBy(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_name = request.query_params.get('query_name', None)
        if ((query_name is None)):
            return Response({'Error': 'Query must include name as query_name'}, status=status.HTTP_400_BAD_REQUEST)
        rents_list = Rents.objects.filter(username=query_name)
        if not rents_list.exists():
            return Response({'Error': 'None rented by requested query_name exists'}, status=status.HTTP_204_NO_CONTENT)
        results = []
        for x in rents_list:
            results.append(RentsSerializer(x).data)
        return Response(results)



### Rents_Out (RENTABLES)

class saveRentOut(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer

# Vehicles that are rentable (Appear in RENTS_OUT table)
class getRentables(generics.ListAPIView):
    serializer_class = Rents_OutSerializer
    def get_queryset(self):
        queryset = Rents_Out.objects.all().select_related('vehicle')
        minPrice = self.request.query_params.get('minPrice', None)
        if minPrice is not None:
            queryset = queryset.filter(daily_rate__gte=minPrice)
        maxPrice = self.request.query_params.get('maxPrice', None)
        if maxPrice is not None:
            queryset = queryset.filter(daily_rate__lte=maxPrice)

        
        partner = self.request.query_params.get('partner', None)
        if partner is not None:
            queryset = queryset.filter(partner=partner)

        return queryset

class deleteRentable(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer

class updateRentable(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer

######################### VEHICLES ##############################

## Helper functions
def filterVehicleQueries(query_params, queryset):
        thequeryset = queryset.objects.all().select_related("vehicle_type")
        manufacturer = query_params.get('manufacturer', None)
        if manufacturer is not None:
            thequeryset = thequeryset.filter(vehicle_type__manufacturer_name=manufacturer)
        return thequeryset




## Vehicle Instances

class getVehicle_Instance(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_sernum = request.query_params.get('query_sernum', None)
        if ((query_sernum is None)):
            return Response({'Error': 'Query must include vehicle serial number as query_sernum'}, status=status.HTTP_400_BAD_REQUEST)
        vehicle_list = Vehicle_Instance.objects.filter(serial_no=query_sernum)
        if not vehicle_list.exists():
            return Response({'Error': 'No Contract with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        return Response(Vehicle_InstanceSerializer(vehicle_list[0]).data)

class getAllVehicle_Instances(generics.ListAPIView):
    queryset = Vehicle_Instance.objects.all()
    serializer_class = Vehicle_InstanceSerializer






## Spacecrafts

class getAvailableSpacecrafts(generics.ListAPIView):
    serializer_class = SpacecraftSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Spacecraft)
        return queryset
class saveSpacecraft(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializerNoNest

class deleteSpacecraft(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializer

class updateSpacecraft(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializerNoNest




## Land Vehicles

class getLand_Vehicles(generics.ListAPIView):
    serializer_class = Land_VehicleSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Land_Vehicle)
        return queryset
class saveLand_Vehicle(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Land_Vehicle.objects.all()
    serializer_class = Land_VehicleSerializerNoNest

class deleteLand_Vehicle(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Land_Vehicle.objects.all()
    serializer_class = Land_VehicleSerializer

class updateLand_Vehicle(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Land_Vehicle.objects.all()
    serializer_class = Land_VehicleSerializerNoNest

## Aircrafts

class getAircrafts(generics.ListAPIView):
    serializer_class = AircraftSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Aircraft)
        return queryset
class saveAircraft(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializerNoNest

class deleteAircraft(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

class updateAircraft(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializerNoNest

## Watercrafts

class getWatercrafts(generics.ListAPIView):
    queryset = Watercraft
    serializer_class = WatercraftSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Watercraft)
        return queryset
class saveWatercraft(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Watercraft.objects.all()
    serializer_class = WatercraftSerializerNoNest

class deleteWatercraft(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Watercraft.objects.all()
    serializer_class = WatercraftSerializer

class updateWatercraft(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Watercraft.objects.all()
    serializer_class = WatercraftSerializerNoNest

## Vehicle Types

class getVehicleTypes(generics.ListAPIView):
    queryset = Vehicle_Type.objects.all()
    serializer_class = Vehicle_TypeSerializer
class saveVehicleTypes(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vehicle_Type.objects.all()
    serializer_class = Vehicle_TypeSerializer

class deleteVehicleTypes(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vehicle_Type.objects.all()
    serializer_class = Vehicle_TypeSerializer

class updateVehicleTypes(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vehicle_Type.objects.all()
    serializer_class = Vehicle_TypeSerializer


## Manufacturers
class getManufacturers(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class saveManufacturers(generics.CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class deleteManufacturers(generics.DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class updateManufacturers(generics.RetrieveUpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


## Made spaceship parts
class getSpaceshipParts(generics.ListAPIView):
    queryset = Made_Spaceship_Parts.objects.all()
    serializer_class = Made_Spaceship_PartSerializer

class saveSpaceshipParts(generics.CreateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Made_Spaceship_Parts.objects.all()
    serializer_class = Made_Spaceship_PartSerializer

class deleteSpaceshipParts(generics.DestroyAPIView):
    permission_classes = [PartnerPermission]
    queryset = Made_Spaceship_Parts.objects.all()
    serializer_class = Made_Spaceship_PartSerializer

class updateSpaceshipParts(generics.RetrieveUpdateAPIView):
    permission_classes = [PartnerPermission]
    queryset = Made_Spaceship_Parts.objects.all()
    serializer_class = Made_Spaceship_PartSerializer

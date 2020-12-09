from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

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


######### LICENSES #############

# Saves a licenses' information
# (This is a template view so we don't have to do much work. More complex views will require more work)
class saveLicense(generics.CreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

# Deletes a license
class deleteLicense(generics.DestroyAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

#Update license
class updateLicense(generics.RetrieveUpdateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

#TODO: In the future we may want to consider making this use self.request.user instead of query_params
# Only if we decide to rework permissions
class getLicenses(generics.ListAPIView):
    serializer_class = LicenseSerializer
    def get_queryset(self):
        myrenter = self.request.query_params.get('renter', None)
        queryset = License.objects.all()
        if myrenter is not None:
            queryset = queryset.filter(renter=myrenter)
        return queryset




## License Types
class saveLicenseType(generics.CreateAPIView):
    queryset = License_Type.objects.all()
    serializer_class = LicenseSerializer

class getAllLicense_Types(generics.ListAPIView):
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

class deleteLicenseType(generics.DestroyAPIView):
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

class updateLicenseType(generics.RetrieveUpdateAPIView):
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer


############### USERS ##################

class savePerson(generics.CreateAPIView):
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


class saveClient(generics.CreateAPIView):
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


class saveRenter(generics.CreateAPIView):
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


class savePartner(generics.CreateAPIView):
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


#Returns the info for a "RENTS" object, including the contract associated with it. 
#TODO: Add ability to filter these by user
class getRentInfo(generics.CreateAPIView):
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer

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


"""
executive decision to not make a view for manufacturer
deal with it, chump 
        (⌐■_■)
"""

class saveRentOut(generics.CreateAPIView):
    queryset = Rents_Out.objects.all
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

# Vehicles that are in the RENTS table (Can filter by renter)
class getRentedOutVehicles(generics.ListAPIView):

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

class getAllVehicle_Instances(generics.ListAPIView):
    queryset = Vehicle_Instance.objects.all()
    serializer_class = Vehicle_InstanceSerializer


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


######################### VEHICLES ##############################

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


class getAvailableSpacecrafts(generics.ListAPIView):
    serializer_class = SpacecraftSerializer

    def get_queryset(self):

        queryset = Spacecraft.objects.all().select_related("vehicle_type")
        manufacturer = self.request.query_params.get('manufacturer', None)
        if manufacturer is not None:
            queryset = queryset.filter(vehicle_type__manufacturer_name=manufacturer)
        
        
        return queryset

def filterVehicleQueries(query_params, queryset):
        thequeryset = queryset.objects.all().select_related("vehicle_type")
        manufacturer = query_params.get('manufacturer', None)
        if manufacturer is not None:
            thequeryset = thequeryset.filter(vehicle_type__manufacturer_name=manufacturer)
        return thequeryset


class getLand_Vehicles(generics.ListAPIView):
    serializer_class = Land_VehicleSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Land_Vehicle)
        
        
        return queryset

class getAircrafts(generics.ListAPIView):
    serializer_class = AircraftSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Aircraft)
        return queryset


class getWatercrafts(generics.ListAPIView):
    queryset = Watercraft
    serializer_class = WatercraftSerializer
    def get_queryset(self):
        queryset = filterVehicleQueries(self.request.query_params, Watercraft)
        return queryset

class getVehicleTypes(generics.ListAPIView):
    queryset = Vehicle_Type
    serializer_class = Vehicle_TypeSerializer
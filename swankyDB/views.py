from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

from datetime import datetime, timedelta


# Put this decorator above every view that we want restricted
from django.contrib.auth.decorators import login_required
# @login_required(login_url=OUR_LOGIN_URL)
# This seems to be more for pages than API endpoints

# For API endpoints:
#https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

"""
class name(generics.CreateAPIView):
    queryset = Sometype.objects.all()
    serializer_class = SometypeSerializer

OR

class searchforsomething(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_param = request.query_params.get('query_param', None)
        if ((query_param is None)):
            return Response({'Error': 'Query must include query_param'}, status=status.HTTP_400_BAD_REQUEST)
        some_list = some_list_type.objects.filter(param=query_param)
        if not some_list.exists():
            return Response({'Error': 'No Sometype with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        
                EITHER DO THIS FOR LIST OF RESULTS:
        results = []
        for x in some_list:
            results.append(SometypeSerializer(x.param OR JUST x).data)
        return Response(results)
        
                OR DO THIS FOR SINGLE RESULT:
        return Response(SometypeSerializer(some_list[0]).data)
"""


######### LICENSES #############

# Saves a licenses' information
# (This is a template view so we don't have to do much work. More complex views will require more work)
class saveLicense(generics.CreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class getAllLicense_Types(generics.ListAPIView):
    queryset = License_Type.objects.all()
    serializer_class = License_TypeSerializer

# class getLicense_Type(APIView):
#     def get(self, request):
#         if(request.method != 'GET'):
#             return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
#         query_type = request.query_params.get('query_type', None)
#         if ((query_type is None)):
#             return Response({'Error': 'Query must include license type as query_type'}, status=status.HTTP_400_BAD_REQUEST)
#         license_list = License_Type.objects.filter(type=query_type)
#         if not license_list.exists():
#             return Response({'Error': 'No License of requested type exists'}, status=status.HTTP_204_NO_CONTENT)
#         return Response(Vehicle_InstanceSerializer(license_list[0]).data)


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


############### USERS ##################

"""
figured admins who search for person/client/renter/partner
would be more likely to searh using name instead of ssn (but we could do both)
    |
    |
    |
    V
"""

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

#TODO: Change this to be vehicles rented out by a certain user
class getRentedOutVehicles(generics.ListAPIView):
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer

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


class getVehicleInstances(generics.ListAPIView):
    serializer_class = Vehicle_InstanceSerializer
    def get_queryset(self):
        queryset = Rents_Out.objects.all().select_related('vehicle')
        minPrice = self.request.query_params.get('minPrice', None)
        if minPrice is not None:
            queryset = queryset.filter(daily_rate__gte=minPrice)
        return queryset


class getAvailableSpacecrafts(generics.ListAPIView):
    serializer_class = SpacecraftSerializer

    def get_queryset(self):

        queryset = Spacecraft.objects.all().select_related("vehicle_type")
        manufacturer = self.request.query_params.get('manufacturer', None)
        if manufacturer is not None:
            queryset = queryset.filter(vehicle_type__manufacturer_name=manufacturer)
        
        return queryset

class getAllLand_Vehicles(generics.ListAPIView):
    queryset = Land_Vehicle
    serializer_class = Land_VehicleSerializer


class getAllAircrafts(generics.ListAPIView):
    queryset = Aircraft
    serializer_class = AircraftSerializer


class getAllWatercrafts(generics.ListAPIView):
    queryset = Watercraft
    serializer_class = WatercraftSerializer


class getVehicleTypes(generics.ListAPIView):
    queryset = Vehicle_Type
    serializer_class = Vehicle_TypeSerializer
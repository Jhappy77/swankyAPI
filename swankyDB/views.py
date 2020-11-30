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

class getLicense_Type(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_type = request.query_params.get('query_type', None)
        if ((query_type is None)):
            return Response({'Error': 'Query must include license type as query_type'}, status=status.HTTP_400_BAD_REQUEST)
        license_list = License_Type.objects.filter(type=query_type)
        if not license_list.exists():
            return Response({'Error': 'No License of requested type exists'}, status=status.HTTP_204_NO_CONTENT)
        return Response(Vehicle_InstanceSerializer(license_list[0]).data)

class getLicenses(APIView):
    
    myQueryset = License.objects.all()
    serializer_class = LicenseSerializer

    # def get(self, request):
    #     if(request.method != 'GET'):
    #         return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
    #     query_id = request.query_params.get('query_id', None)
    #     if ((query_id is None)):
    #         return Response({'Error': 'Query must include license id as query_id'}, status=status.HTTP_400_BAD_REQUEST)
    #     license_list = License.objects.filter(license_id=query_id)
    #     if not license_list.exists():
    #         return Response({'Error': 'No License with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
    #     return Response(LicenseSerializer(license_list[0]).data)


############### USERS ##################

"""
figured admins who search for person/client/renter/partner
would be more likely to searh using name instead of ssn (but we could do both)
    |
    |
    |
    V
"""
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

#TODO: Change this to be vehicles rented out by a certain user
class getRentedOutVehicles(generics.ListAPIView):
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer

#TODO: 
class getAllVehicle_Instances(generics.ListAPIView):
    queryset = Vehicle_Instance.objects.all()
    serializer_class = Vehicle_InstanceSerializer


class getAllRented(generics.ListAPIView):
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer

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


class getAllSpacecrafts(generics.ListAPIView):
    queryset = Spacecraft
    serializer_class = SpacecraftSerializer


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
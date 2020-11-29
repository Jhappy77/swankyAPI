from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

from datetime import datetime, timedelta

"""
we should probably add some authentication stuff, so for example
only admins can search for persons/renters/etc. or for a license
is that what you also meant here?
                                |
                                |
                                V
"""
# Don't do anything with the User Model just yet. Django has some predefined user
# stuff that we should probably use instead, I will look into it tomorrow morning

# Saves a licenses' information
# (This is a template view so we don't have to do much work. More complex views will require more work)
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


class saveLicense(generics.CreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


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


class getContracts(generics.CreateAPIView):
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


"""
executive decision to not make a view for manufacturer
deal with it, chump 
        (⌐■_■)
"""


class getRentedOutVehicles(generics.CreateAPIView):
    queryset = Rents_Out.objects.all()
    serializer_class = Rents_OutSerializer


"""
could have another to search for a certain kind of vehicle...
"""


class getAllVehicle_Instances(generics.CreateAPIView):
    queryset = Vehicle_Instance.objects.all()
    serializer_class = Vehicle_InstanceSerializer


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


class getAllSpacecrafts(generics.CreateAPIView):
    queryset = Spacecraft
    serializer_class = SpacecraftSerializer


class getAllLand_Vehicles(generics.CreateAPIView):
    queryset = Land_Vehicle
    serializer_class = Land_VehicleSerializer


class getAllAircrafts(generics.CreateAPIView):
    queryset = Aircraft
    serializer_class = AircraftSerializer


class getAllWatercrafts(generics.CreateAPIView):
    queryset = Watercraft
    serializer_class = WatercraftSerializer


class getVehicleTypes(generics.CreateAPIView):
    queryset = Vehicle_Type
    serializer_class = Vehicle_TypeSerializer


"""
USERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSER
user stuff goes here USERUSERUSERUSERUSERUSERUSERUSER
USERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSERUSER
"""


class getAllLicense_Types(generics.CreateAPIView):
    queryset = License_Type
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


class getLicense(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        query_id = request.query_params.get('query_id', None)
        if ((query_id is None)):
            return Response({'Error': 'Query must include license id as query_id'}, status=status.HTTP_400_BAD_REQUEST)
        license_list = License.objects.filter(license_id=query_id)
        if not license_list.exists():
            return Response({'Error': 'No License with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        return Response(LicenseSerializer(license_list[0]).data)


class getAllRented(generics.CreateAPIView):
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


"""
this was clutch. thanks!!!
  |
  |
  V
"""
# If you want to make views, you can see the views I made at https://github.com/Jhappy77/swagadellicAPI/tree/main/swagDB in views.py for inspiration

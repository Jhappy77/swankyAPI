from swankyDB.serializers import ClientSerializer, RenterSerializer
from rest_framework import permissions
from .models import Client, Renter, Partner, Admin_User


# If there is a renter object associated with this user
class RenterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        client = Client.objects.filter(username=request.user.id)
        if not client.exists():
            return False
        clientID = client[0].id
        renter = Renter.objects.filter(client=clientID)
        return renter.exists()

# If a partner object is associated with this user
class PartnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        client = Client.objects.filter(username=request.user.id)
        if not client.exists():
            return False
        clientID = client[0].id
        partner = Partner.objects.filter(client=clientID)
        return partner.exists()


def getRenterID(request):
    client = Client.objects.filter(username=request.user.id)
    if not client.exists():
        raise Exception('No client exists with that id')
    clientID = client[0].id
    renter = Renter.objects.filter(client=clientID)
    if not renter.exists():
        raise Exception('No client exists with that id')
    return renter[0].id

def getPartnerID(request):
    client = Client.objects.filter(username=request.user.id)
    if not client.exists():
        raise Exception('No client exists with that id')
    clientID = client[0].id
    partner = Partner.objects.filter(client=clientID)
    if not partner.exists():
        raise Exception('No client exists with that id')
    return partner[0].id


# ░░█▀░░░░░░░░░░░▀▀███████░░░░ 
# ░░█▌░░░░░░░░░░░░░░░▀██████░░░ 
# ░█▌░░░░░░░░░░░░░░░░███████▌░░ 
# ░█░░░░░░░░░░░░░░░░░████████░░ 
# ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ 
# ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ 
# ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ 
# ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ 
# ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ 
# ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ 
# ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ 
# ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ 
# ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ 
# ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ 
# ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ 
# ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ 
# ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ 
# ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ 
# ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ 
# ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ 
# ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ 
# ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ 
# ░░▄▌████████▄▄▄███████▌░░░░░▄ 
# ░▄▀░██████████████████▌▀▄░░░░ 
# ▀░░░█████▀▀░░░▀███████░░░▀▄░░ 
# ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ 
# ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ 
# ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ 
# you have been visited by BarASCII Obama
# say "thank obama" within 3 seconds or you will be banished to the shadow realm
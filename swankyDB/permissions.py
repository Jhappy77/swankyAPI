from swankyDB.serializers import ClientSerializer, RenterSerializer
from rest_framework import permissions
from .models import Client, Renter, Partner, Admin_User


# If there is a renter object associated with this user
class RenterPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        client = Client.objects.filter(username=request.user.id)
        if not client.exists():
            return False
        print(ClientSerializer(client))
        clientID = client[0].id
        print(clientID)
        renter = Renter.objects.filter(client=clientID)
        #renter = client.renters_set
        print(RenterSerializer(renter))
        return renter.exists()


class PartnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return super().has_permission(request, view)



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
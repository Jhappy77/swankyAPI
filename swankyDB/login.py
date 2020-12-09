from swankyDB.serializers import UserSerializer
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User

class login_view(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"msg": "Your login was successful!"})
        else:
            return Response({"error": "Could not validate your login information"}, status=status.HTTP_401_UNAUTHORIZED)

class signup_view(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

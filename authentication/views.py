from django.shortcuts import render
from serializer import UserRegistrationSerializer, LoginSerializer
from rest_auth.registration.views import RegisterView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

def index(self):
    return render(self,"index.html")

class userRegistrationView(RegisterView):
    serializer_class = UserRegistrationSerializer

def check_user_acc(request):
    tokens = Token.objects.filter(user=request.user)
    for token in tokens:
        user = Token.objects.get(key=token).user

    return user.manager

class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        data = {}


        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)

            # user_manager = Token.objects.get(key=token).user.is_driver
            # if user_manager:
            #     user_role = 'Driver'
            # else:
            #     user_role = 'Customer'

            data['token'] = token.key
            # data['User_role'] = user_role
            data['id'] = user.id

        else:
            data = serializer.errors

        return Response(data)

from django.shortcuts import render
from authentication.serializer import  LoginSerializer
from rest_auth.registration.views import RegisterView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers
from rest_framework import status
from authentication.serializer import UserSerializer, UserUpdateSerializer, UserDisplaySerializer
# from django.contrib.auth.models import User
from .models import User


# Create your views here.

def index(self):
    return render(self,"index2.html")

# class userRegistrationView(RegisterView):
#     serializer_class = UserRegistrationSerializer
#     def get_cleaned_data(self):
#             data = super(UserRegistrationSerializer,self).get_cleaned_data()
#             return data

#     def save(self, request):
#         user = super(UserRegistrationSerializer)
#         user.save()
#         return user

# def check_user_acc(request):
#     tokens = Token.objects.filter(user=request.user)
#     for token in tokens:
#         user = Token.objects.get(key=token).user

#     return user.manager



class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class User_Update(APIView):
    def put(self,request, pk):
        item = User.objects.get(pk=pk)
        data = UserUpdateSerializer(instance=item, data=request.data)
    
        if data.is_valid():
            item.bio =request.data['bio']
            item.avatar =request.data['avatar']
            item.email =request.data['email']
            item.save()
            return Response(data.data)
        else:
            return Response("VALUES SUPPLIED NOT VALID", status=status.HTTP_404_NOT_FOUND)

class UserDisplay(APIView):
    
    def get(self, request):
        users = User.objects.all()
        serializers = UserDisplaySerializer(users, many=True)

        return Response(serializers.data)





from django.shortcuts import render
from serializer import UserRegistrationSerializer, LoginSerializer
from rest_auth.registration.views import RegisterView


# Create your views here.

def index(self):
    return render(self,"index.html")

class userRegistrationView(RegisterView):
    serializer_class =UserRegistrationSerializer

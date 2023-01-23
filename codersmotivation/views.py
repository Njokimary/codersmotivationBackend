from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    # now =datetime.now()
    message="hello we are learning Django and we are enjoying it"
    return render(request,"index.html",{"message":message})




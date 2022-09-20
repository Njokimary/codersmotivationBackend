from django.urls import path
# from authentication.views import DriverRegistrationView, CustomerRegistrationView
from . import views

# app_name = 'booking'

urlpatterns = [
    #Registration Urls
    path('', views.index, name='index'),
    # path('registration/driver/', DriverRegistrationView.as_view(), name='driver'),
    # path('registration/customer/', CustomerRegistrationView.as_view(), name='register-customer'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]



from django.urls import path
from authentication.views import userRegistrationView, LoginView
from . import views

# app_name = 'booking'

urlpatterns = [
    #Registration Urls
    path('', views.index, name='index'),
    path('registration/',userRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]



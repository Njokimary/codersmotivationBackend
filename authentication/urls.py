from django.urls import path, include
from authentication.views import  LoginView
from . import views
# from django.contrib.auth import views
# app_name = 'booking'

urlpatterns = [
    #Registration Urls
    path('/registration',views.UserCreate.as_view(), name='register'),
    path('/login', views.LoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/update_user/<pk>/', views.User_Update.as_view() )
]



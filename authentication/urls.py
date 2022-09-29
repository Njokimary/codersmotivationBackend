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
    # path('logout/', views.LogoutView.as_view(), {"next_page": '/'}), 
    # path('login', views.redirect_to_login,{"next_page": 'home'}),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('logout/', views.LogoutView.as_view(), name='logout'),
]



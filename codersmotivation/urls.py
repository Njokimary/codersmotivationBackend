from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('home', views.home ,name="home")
    path('api/post/', views.Postapi.as_view()),
    # path('api/profile/', views.profile_update.as_view()),
    # path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
]
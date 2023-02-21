from django.urls import path
from . import views
from .views import LikeView, UnlikeView

urlpatterns = [
    path('', views.index, name="index"),
    # path('home', views.home ,name="home")
    path('api/post/', views.Postapi.as_view()),
    # path('api/profile/', views.profile_update.as_view()),
    # path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api/like/',views.Like .as_view()),
    # path('likes/', views.LikeAPIView.as_view(), name='like_api'),
    path('posts/<int:pk>/like/', LikeView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view()),
]
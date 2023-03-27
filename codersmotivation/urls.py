from django.urls import path
from . import views
from .views import LikeView, UnlikeView

urlpatterns = [
    path('', views.index, name="index"),
    # path('home', views.home ,name="home")
    path('api/post/', views.Postapi.as_view()),
    path('comments/', views.CommentAPIView.as_view(), name='comment_api'),
    path('comments/<int:pk>', views.CommentAPIView.as_view(), name='comment_api_get'),
    path('posts/<int:pk>/like/', LikeView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view()),
    path('posts/', views.post_list, name='post_list'),
    path('post_delete/<pk>/', views.Post_Delete.as_view() ),
]
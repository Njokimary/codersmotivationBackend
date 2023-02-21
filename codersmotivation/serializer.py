from rest_framework import serializers
from .models import Post, Comment
from authentication.models import User
from rest_framework.response import Response

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ('id', 'user', 'liked_object_id', 'created_at')
#         read_only_fields = ('id', 'created_at')


# serializers.py

from rest_framework import serializers
from .models import Post, Comment

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'likes')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created_at')
        read_only_fields = ('id', 'created_at')
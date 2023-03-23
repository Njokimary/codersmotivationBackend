from rest_framework import serializers
from .models import Post, Comment
from authentication.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):
    
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments', 'author')

    author = UserSerializer(read_only=True)
        
    def get_comments(self, post):
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    





class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'likes')




class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'author','post', 'text', 'created_on')
        # read_only_fields = ('id', 'created_on','author')
        
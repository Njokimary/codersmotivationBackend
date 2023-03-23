from rest_framework import serializers
from .models import Post, Comment
from authentication.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Post
    #     fields = '__all__'

    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments', 'author')

    author = UserSerializer(read_only=True)
        
    def get_comments(self, post):
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    




from rest_framework import serializers
from .models import Post, Comment

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'likes')


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'author', 'text', 'created_at')
#         read_only_fields = ('id', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author','post', 'text', 'created_on')
        read_only_fields = ('id', 'created_on')
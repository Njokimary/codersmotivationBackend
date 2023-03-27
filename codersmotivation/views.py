from django.shortcuts import render
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Post as Post, User, Comment
from rest_framework import status
from .serializer import PostSerializer, CommentSerializer
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from .serializer import LikeSerializer
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    # now =datetime.now()
    message="hello we are learning Django and we are enjoying it"
    return render(request,"index.html",{"message":message})



class Postapi(APIView):
    # def get(self, request, format=None):
    #     # all_post = Post.objects.all()
    #     # serializers = PostSerializer(all_post, many=True)


    #     posts = Post.objects.all()
    #     data = []
    #     for post in posts:
    #         comments = Comment.objects.filter(post=post)
    #         data.append({
    #             'id': post.id,
    #             'title': post.title,
    #             'content': post.content,
    #             'comments': [{'id': comment.id, 'text': comment.text} for comment in comments]
    #         })


    #     return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
   
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


class Post_Delete(APIView):
    def delete(self,request, pk):
        item = Post.objects.get(id=pk)
        
        if item :
            item.delete()
            return Response("post deleted")
        else:
            return Response("post not found", status=status.HTTP_404_NOT_FOUND)





class LikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class UnlikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like -= 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def get(self, request, pk):
        post_comment = Comment.objects.filter(post =pk)
        serializers = CommentSerializer(post_comment, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = serializer.validated_data.get('post' )
        author = serializer.validated_data.get('author')
        text = serializer.validated_data.get('text')

        comment = Comment(author=author, text=text, post = post)
        comment.save()



        return Response({'detail': 'Comment created.', 'comment': self.serializer_class(comment).data}, status=status.HTTP_201_CREATED)



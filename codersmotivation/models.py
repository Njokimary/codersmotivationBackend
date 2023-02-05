# from tkinter import CASCADE
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import User

class Category(models.Model):
  category =models.CharField(max_length=20)

  def __str__(self):
      return self.category

class Post(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title =models.CharField(max_length=20)
  image = CloudinaryField('image')
  video = CloudinaryField('video')
  content =models.TextField
  time_posted =models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  like = models.IntegerField(default=0)

  
  objects = models.Manager()

  def __str__(self):
      return self.title


  
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class Likes(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    bio = models.TextField()
    email = models.EmailField(default="@user.com")
    # category =models.ForeignKey(Category, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
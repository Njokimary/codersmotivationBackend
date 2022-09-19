from tkinter import CASCADE
from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_admin = models.BooleanField(default=False)
  is_staff= models.BooleanField(default=False)
  def __str__(self):
      return self.username

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
  likes = models.IntegerField(default=0)
  
  


  def __str__(self):
      return self.category


  
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


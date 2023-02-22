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

  def likes_count(self):
       return self.like.all().count()

  def __str__(self):
      return self.title


  
class Comment(models.Model):
    # post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment "{}" by {}'.format(self.text, self.author)

# class Likes(models.Model):
#     post =models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

    
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     liked_object_id = models.PositiveIntegerField()
#     # liked_object_type = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)


from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_admin = models.BooleanField(default=False)
  is_staff= models.BooleanField(default=False)
  def __str__(self):
      return self.username
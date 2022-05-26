from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = models.CharField(max_length=50,default='Anonymous')
  email=models.EmailField(max_length=100,unique=True)
  image_password = models.CharField(max_length=100,blank=True)
  authenticated=models.BooleanField(default=False)

  USERNAME_FIELD="email"
  REQUIRED_FIELDS=["username"]

  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
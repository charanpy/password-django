from django.db import models

from api.user.models import CustomUser

class ImageAuth(models.Model):
  userId=models.ForeignKey(CustomUser,on_delete=models.SET_NULL, blank=True, null=True)
  password = models.CharField(max_length=150)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)


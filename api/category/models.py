from turtle import update
from django.db import models


class Category(models.Model):
  name=models.CharField(max_length=20,unique=True)
  created_at = models.DateTimeField(auto_now=True,blank=False)

  def __str__(self) -> str:
      return self.name


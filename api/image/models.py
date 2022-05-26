from django.db import models
from api.category.models import Category

# Create your models here.
class Image(models.Model):
  name=models.CharField(max_length=50,unique=True)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  category=models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
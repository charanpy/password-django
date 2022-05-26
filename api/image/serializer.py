
from rest_framework import serializers

from .models import Image

class ImageSerializer(serializers.HyperlinkedModelSerializer):
  image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
  
  class Meta:
    model=Image
    fields=('id','image','name','category')
    # depth=1
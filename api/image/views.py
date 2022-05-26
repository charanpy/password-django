from rest_framework import viewsets

from .models import Image
from .serializer import ImageSerializer

class ImageViewSets(viewsets.ModelViewSet):
  queryset=Image.objects.all().order_by('id')
  serializer_class=ImageSerializer

  def get_queryset(self):
      queryset = Image.objects.all().order_by('id')
      category = self.request.query_params.get('category')

      if category is not None:
        queryset = queryset.filter(category_id=category)

      print(queryset)
      return queryset
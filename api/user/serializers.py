from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import CustomUser
from api.imageAuth.models import ImageAuth

class UserSerializer(serializers.HyperlinkedModelSerializer):

  def create(self, validated_data):
      password = validated_data.pop('password',None)
      image_password = validated_data.pop('image_password',None)

      if(not password or not image_password):
        raise serializers.ValidationError(detail="Invalid Credentials",code=400)
      instance = self.Meta.model(**validated_data)

      if password is not None:
        instance.set_password(password)

      instance.save()

      ImageAuth.objects.create(password=make_password(image_password),userId=instance)
      
      return instance

  class Meta:
    model=CustomUser
    extra_kwargs = {'password': {'write_only': True}}
    fields = ('username', 'email', 'password','image_password',
                  )

from rest_framework import serializers

from .models import ImageAuth


class ImageAuthSerializer(serializers.HyperlinkedModelSerializer):
  def create(self, validated_data):
      password = validated_data.pop('password')
      instance = self.Meta.model(**validated_data)


      if (not password):
        raise serializers.ValidationError(detail="Invalid Credentials",code=400)

      instance.save()
      return instance

  class Meta:
      model=ImageAuth
      extra_kwargs = {'password': {'write_only': True}}
      fields = ('userId','password')
      depth=1


      
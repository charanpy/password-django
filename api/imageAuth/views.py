from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login

from api.user.models import CustomUser

from .models import ImageAuth
from .serializers import ImageAuthSerializer

@api_view(['POST'])
def authenticateByImage(request):
  password = request.data.get('password',False)
  userId = request.data.get('userId',False)

  try:
    data_dict = ImageAuth.objects.filter(
               userId_id = userId ).values().first()
    
    user=CustomUser.objects.get(pk=userId)
    
    

    print(user)
    if check_password(password,data_dict.get('password')):
      token,_ = Token.objects.get_or_create(user=user)
      login(request,user)
      return Response({
        "token":token.key,
      })
    else:
      return Response({"message":'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)

  except ImageAuth.DoesNotExist:
    return Response({"message":'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

class ImageAuthViewSet(viewsets.ModelViewSet):
  permission_classes_by_action= {'create': [AllowAny]}
  queryset = ImageAuth.objects.all().order_by('id')
  serializer_class=ImageAuthSerializer

  def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]

 


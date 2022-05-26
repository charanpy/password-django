from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

from .serializers import UserSerializer

from .models import CustomUser

@api_view(['POST'])
def login(request):
  print(request.data)
  email = request.data.get('email',False)
  password = request.data.get('password',False)

  if (not email or not password):
    return Response({"message":'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)

  UserModel = get_user_model()

  try:

    user = UserModel.objects.get(email=email)
   
    if user.check_password(password):
      user_dict = UserModel.objects.filter(
                email=email).values().first()
      
      return Response({"id":user_dict.get('id'),"email":user_dict.get('email')})
    else:
      return Response({"message":'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)

  except UserModel.DoesNotExist:
    return Response({"message":'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logOut(request):
  try:
    request.user.auth_token.delete()
    return Response({})
  except:
    return Response({"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMe(request):
  try: 
    UserModel = get_user_model()
    user_dict = UserModel.objects.filter(
                id=request.user.id).values().first()
    
    return Response({
      "email":user_dict.get('email'),
      "username": user_dict.get("username"),
      "id":user_dict.get("id")
    })
  except:
    return Response({"message":'Not Found'},status=status.HTTP_404_NOT_FOUND)



class UserViewSet(viewsets.ModelViewSet):
  permission_classes_by_action= {'create': [AllowAny]}
  queryset = CustomUser.objects.all().order_by('id')
  serializer_class=UserSerializer

  def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]

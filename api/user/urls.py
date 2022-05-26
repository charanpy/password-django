from rest_framework import routers

from django.urls import path,include

from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns=[
  path('login/',views.login),
  path('logout/',views.logOut),
  path('me/',views.getMe),
  path('',include(router.urls)),
]
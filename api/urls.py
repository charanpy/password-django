
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.hello),
    path('category/',include('api.category.urls')),
    path('user/',include('api.user.urls')),
    path('image-auth/',include('api.imageAuth.urls')),
    path('image/',include('api.image.urls'))

]

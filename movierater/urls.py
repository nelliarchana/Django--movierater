from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls') ),
    path('auth/',obtain_auth_token),

]

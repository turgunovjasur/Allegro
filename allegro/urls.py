from django.contrib.auth import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('', admin.urls)
]

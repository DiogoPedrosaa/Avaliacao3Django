
from django.contrib import admin
from django.urls import path, include
from GymApp import urls as GymApp_urls

urlpatterns = [
    path('', include(GymApp_urls)),
]

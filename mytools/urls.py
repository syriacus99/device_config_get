from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
urlpatterns = [
    path('load_file/',views.load_file),
    path('load_device_info/',views.load_device_info)
]
from django.contrib import admin
from django.urls import path,re_path,include
from app_auth import views


app_name='app_auth'

urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^index/$',views.index,name='index'),
]
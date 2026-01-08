from first_app import views
from django.conf.urls import url
from django.urls import path,re_path

urlpatterns = [
    re_path(r"^$", views.index, name='index'),


]
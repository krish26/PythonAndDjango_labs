from django.contrib import admin
from django.urls import path,include
from employee_data import views


app_name='employee_data'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('preview/<int:user_id>/',views.preview,name='preview'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')

]

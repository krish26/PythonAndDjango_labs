from django.urls import path,re_path,include
from books_app import views

urlpatterns = [
    re_path(r'^$',views.home,name='home'),
    re_path(r'^bookshelf/$',views.bookshelf,name='bookshelf'),
    re_path(r'^about/$',views.about,name='about'),
    
]
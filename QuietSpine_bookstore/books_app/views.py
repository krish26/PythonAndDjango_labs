from django.shortcuts import render
from django.http import HttpResponse
from .models import booknames

def home(request):
    return render(request,'books_app/home.html')

def bookshelf(request):
    context={'books':booknames.objects.all()}
    return render(request,'books_app/bookshelf.html',context)

def about(request):
    return render(request,'books_app/about.html')

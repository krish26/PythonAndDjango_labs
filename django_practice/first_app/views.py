from django.shortcuts import render
from django.http import HttpResponse


my_dict = { 'message':'Welcome ',
                 'course': 'Python Ai and ML course',
                  'days': 60,
                  'name':'krishna koumudi'
            }

def index(request):
    context={'my_dict': my_dict}
    return render(request, 'first_app/index.html', context)

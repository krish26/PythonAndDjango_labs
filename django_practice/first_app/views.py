from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord


def index(request):
    webpages=Webpage.objects.all()
    Acc_records=AccessRecord.objects.all()
    context={
        'webpages':webpages,
        'Acc_records':Acc_records
    }
    return render(request, 'first_app/index.html',context)
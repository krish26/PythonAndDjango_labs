from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord


def index(request):
    acc_records=AccessRecord.objects.order_by('date')
    date_dict={'access_records':acc_records}
    return render(request, 'first_app/index.html',context=date_dict)
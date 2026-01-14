from django.shortcuts import render,redirect
from app_form import forms
#from django.contrib import messages
from app_form.forms import newTicketForm


def home_ticket(request):
    form=newTicketForm()

    if request.method=='POST':
        form=newTicketForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home_ticket(request)
        else:
            print("form is invalid")
    return render(request,'app_form/ticket_form.html',{'form':form})

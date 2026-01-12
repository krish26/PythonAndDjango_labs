from django.shortcuts import render,redirect
from app_form import forms
from django.contrib import messages


def home_ticket(request):
    form=forms.InputForm()
    if request.method=='POST':
        form=forms.InputForm(request.POST)

        if form.is_valid():  
            print("Form is valid")
            print("Full Name:",form.cleaned_data.get('full_name'))
            print("Email:",form.cleaned_data.get('email'))
            print("Textarea:",form.cleaned_data.get('textarea'))                
            print("Category:",form.cleaned_data.get('Category'))
            messages.success(
                request,
                "Ticket submitted successfully."
            )
            return redirect('home')
        
        else:
            print("Form is invalid")
    return render(request,'app_form/ticket_form.html',{'form':form})

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from employee_data.forms import AccountDetailsForm,OnboardingDetailsForm
from employee_data.models import EmployeeProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def home(request):
    return render(request, 'employee_data/home.html')

@login_required
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
     login(request)


def register(request):
    registered=False
    user_id=None

    if request.method == 'POST':
        #create forms instances 
        account_form=AccountDetailsForm(request.POST)
        onboarding_form=OnboardingDetailsForm(request.POST,request.FILES)   #images should contain request.files tag

        #validate forms 

        if account_form.is_valid() and onboarding_form.is_valid():
            #save user 
            user=account_form.save()
            user.set_password(user.password) #hash ps
            user.save()

            #save emp profile
            profile=onboarding_form.save(commit=False)
            profile.user=user
            profile.save()

            registered=True
            user_id=user.id

        else:
            messages.error(request,'Please correct the errors')

    else:
        account_form=AccountDetailsForm()
        onboarding_form=OnboardingDetailsForm()
    
    return render(request,'employee_data/register.html',
                  {
                      'account_form':account_form,
                      'onboarding_form':onboarding_form,
                      'registered':registered,
                      'user_id':user_id
                  })


def preview(request,user_id):
        
        user = get_object_or_404(User, id=user_id)
        profile = get_object_or_404(EmployeeProfileInfo, user=user)
        return render(request, 'employee_data/preview.html', 
                      {
                        'user': user,
                        'profile': profile
                      })


def user_login(request):
     if request.method =='POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          #django builtin authentication

          user = authenticate(username=username,password=password)
          if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('employee_data/home.html'))
                else:
                     return HttpResponse("ACCOUNT NOT ACTIVE")
          else:
               print('someone tried to login and failed')
               print('username:{} and password:{}'.format(username,password))
          return HttpResponse("invalid login detailes")
     else:
          return render(request,'employee_data/login.html')
               
          



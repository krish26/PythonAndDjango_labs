from django.shortcuts import render
from app_auth.forms import Userform,UserProfileInfoForm

def index(request):
    return render(request,'app_auth/index.html')

def register(request):
    registered=False
    if request.method=='POST':
        user_form = Userform(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=Userform()
        profile_form=UserProfileInfoForm()


    return render(request,'app_auth/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered
                   }
                  )




from django import forms
from django.contrib.auth.models import User
from employee_data.models import EmployeeProfileInfo


class AccountDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class OnboardingDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfileInfo
        fields = ('portfolio_site', 'profile_pic')

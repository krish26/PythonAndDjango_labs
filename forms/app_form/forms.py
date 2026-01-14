from django import forms
from .models import ticket

class InputForm(forms.Form):
    full_name = forms.CharField()
    email=forms.CharField(widget=forms.EmailInput)
    textarea=forms.CharField(widget=forms.Textarea)
    Category =forms.ChoiceField(choices=[('','Select'),('login_problem','Login_problems'),('payment','payment'),('bug report','bug report')])

    def clean_full_name(self):  
        name = self.cleaned_data.get('full_name').strip()
        parts=name.split()
        if len(parts)<2:
            raise forms.ValidationError("Please enter your full name")
        return name
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('.com') or '@' not in email:
            raise forms.ValidationError("Email must end with .com")
        return email
    
    def clean_textarea(self):
        textarea=self.cleaned_data.get('textarea')
        if len(textarea)<20:
            raise forms.ValidationError("Please provide more details (at least 20 characters).")
        return textarea
    
class newTicketForm(forms.ModelForm):
        class Meta:   #inline class
            model = ticket
            fields = '__all__'

        full_name = forms.CharField()
        email=forms.CharField(widget=forms.EmailInput)
        textarea=forms.CharField(widget=forms.Textarea)
        Category =forms.ChoiceField(choices=[('','Select'),('login_problem','Login_problems'),('payment','payment'),('bug report','bug report')])

        def clean_full_name(self):  
            name = self.cleaned_data.get('full_name').strip()
            parts=name.split()
            if len(parts)<2:
                raise forms.ValidationError("Please enter your full name")
            return name
    
        def clean_email(self):
            email=self.cleaned_data.get('email')
            if not email.endswith('.com') or '@' not in email:
                raise forms.ValidationError("Email must end with .com")
            return email
    
        def clean_textarea(self):
                textarea=self.cleaned_data.get('textarea')
                if len(textarea)<20:
                    raise forms.ValidationError("Please provide more details (at least 20 characters).")
                return textarea

        

        
        


  

        

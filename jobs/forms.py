from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator


class RegistationForm(UserCreationForm):
    email = forms.EmailField(label='email',validators=[EmailValidator],error_messages={"invalid":'This is invalid email address'})
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']





class CompanyDetailForms(forms.ModelForm):
    class Meta:
        model = CompanyeeDetails
        labels = {
            "com_name":'company name',
            "com_email": 'company Email',
            "com_city" : 'company City',
            "com_address":'company address',
            "com_logo" : 'company Logo',
        }
        exclude = ('user',)



class ApplyForms(forms.ModelForm):
    class Meta:
        model = Apply
        labels = {
            "first_name" : 'First Name',
            'last_name' : 'Last Name',
            'contact': 'Contact',
            'email' : 'Email Id ',
            'city':'City',
            "address ": 'Address',
            'state' : 'State',
            'resume': 'Resume',
        }
        exclude = ('user','status','job_id','date',)



class AddJobsForms(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ('com_id','datetime')
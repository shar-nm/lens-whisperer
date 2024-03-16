
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField()    
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
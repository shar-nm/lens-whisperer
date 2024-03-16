
from django import forms
from .models import UserRegister


class SignupForm(forms.Form):
    class Meta:
        model = UserRegister
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
    
    first_name = forms.CharField()
    last_name = forms.CharField() 
    username = forms.CharField()    
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
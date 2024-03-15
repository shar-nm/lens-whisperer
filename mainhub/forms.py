from .models import UserRegister
from django import forms


class SignupForm(forms.Form):
    class Meta:
        model = UserRegister
        fields = ('username', 'email', 'password1', 'password2')
    
    first_name = forms.CharField()
    last_name = forms.CharField() 
    username = forms.CharField()    
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
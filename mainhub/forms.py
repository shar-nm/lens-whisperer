from .models import UserRegister
from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ('first_name', 'last_name','email', 'password1','password2')


first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Surname',
        'class': 'w-full py-4 px-6 rounded-xl'
     }))

    
email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
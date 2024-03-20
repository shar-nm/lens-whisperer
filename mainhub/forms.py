from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



INPUT_CLASSES = 'form-control'


class SignupForm(UserCreationForm):  
   
     class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')


        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
             'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            }

     def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

               






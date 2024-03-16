from django.shortcuts import render, redirect
from .forms import SignupForm



# Create your views here.


def mainhub(request):
    return render(request, 'mainhub/main.html')




def signup(request):
    context = {'form': SignupForm}
    return render(request, 'mainhub/signup.html', context)











     
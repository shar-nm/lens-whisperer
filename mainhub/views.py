from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm



# Create your views here.


def mainhub(request):
    return render(request, 'mainhub/main.html')




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you are now signed up !')
            return redirect('home')

    else:
           form = SignupForm()

    
    return render(request, 'registration/signup.html', {
        'form': form
    })


def login_user(request):
    if request.method == "POST":
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('home')
        
       else:
           messages.warning(request, ('There was an error, please log in...'))
           return redirect('login')

    else:
        messages.warning(request, 'error, try again !')
        return render(request,'registration/login.html',{})



def logout_user(request):
    logout(request)
    messages.warning(request,('You are now logged out!'))
    return redirect('mainhub')




     
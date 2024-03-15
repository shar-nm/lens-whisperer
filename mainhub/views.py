from django.shortcuts import render
from article.models import Category, Article
from .forms import SignupForm



# Create your views here.


def mainhub(request):
    return render(request, 'mainhub/main.html')



def signup(request):
     if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
    
     else:
        form = SignupForm()

     return render(request, 'mainhub/signup.html', {
        'form': form
    })
from django.shortcuts import render
from .models import Category, Article

# Create your views here.


def index(request):
    return render(request, 'article/index.html')
   






   

   
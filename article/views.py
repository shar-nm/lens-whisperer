from django.shortcuts import render
from .models import Category, Article

# Create your views here.


def article(request):
    return render(request, 'article/articles.html')
   






   

   
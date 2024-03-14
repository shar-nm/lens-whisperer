from django.shortcuts import render
from article.models import Category, Article



# Create your views here.


def mainhub(request):
    return render(request, 'mainhub/main.html')


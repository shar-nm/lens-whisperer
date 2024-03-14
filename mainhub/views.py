from django.shortcuts import render
from article.models import Category, Article



# Create your views here.


def index(request):
    return render(request, 'mainhub/index.html')


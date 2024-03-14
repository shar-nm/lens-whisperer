from django.shortcuts import render
from .models import Category, Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    return render(request, 'article/index.html',{
        'categories': categories,
        'articles': articles,
    })

   






   

   
from django.shortcuts import render
from .models import Category, Article, Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    images = Article.objects.all()


    return render(request, 'article/index.html', {
        'categories': categories,
         'articles': articles,
         'images': images,
    }) 
        




   

   
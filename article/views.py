from django.shortcuts import render, get_object_or_404
from .models import Category, Article

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


def article_details(request,pk):
    article = get_object_or_404(Article, pk=pk)
    
    return render(request, 'article/article-details.html', {
        'article': article,
    })

        




   

   
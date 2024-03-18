from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import NewArticleForm
from .models import Category, Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    category = None
    if request.GET:
        if "category" in request.GET:
            category = request.GET["category"]
            articles = articles.filter(category=category)

    template = 'article/index.html'
    context = {
        'categories': categories,
        'articles': articles,
    }
    return render(request, template, context) 


def article_details(request,pk):
    article = get_object_or_404(Article, pk=pk)
    
    return render(request, 'article/article-details.html', {
        'article': article,
    })

        
@login_required
def new(request): 
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article successfully added!")

            return redirect('article-details', pk=article.id)
    else:
        form = NewArticleForm()

    return render(request, 'article/new-article.html', {
        'form': form,
        'title': 'Create article',
    })

   

   

   
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewArticleForm
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

        
@login_required
def new(request): 
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()

            return redirect('article:article_detail', pk=article.id)
    else:
        form = NewArticleForm()

    return render(request, 'article/new-article.html', {
        'form': form,
        'title': 'Create article',
    })

   

   

   
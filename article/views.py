from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import NewArticleForm, EditArticleForm, ReviewForm
from .models import Category, Article, Review
from django.core.paginator import Paginator
# Create your views here.




def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    category = None
    if request.GET:
        if "category" in request.GET:
            category = request.GET["category"]
            articles = articles.filter(category=category)
    
    p = Paginator( Article.objects.all(), 6)
    page = request.GET.get('page')
    articles = p.get_page(page)

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


@login_required
def edit(request, pk): 
    article = get_object_or_404(Article, pk=pk, author=request.user)

    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully edited!")
            return redirect('article-details', pk=article.pk)
    else:
        form = EditArticleForm(instance=article)

    
    return render(request, 'article/new-article.html', {
        'form': form,
        'title': 'Edit article',
    })




@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.delete()
    messages.success(request, "article deleted!")
    return redirect('dashboard:dashboard')

   

   
def review_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    reviews = article.reviews.all().order_by("-created_at")
    review_count = article.reviews.count()

    if request.method == "POST":
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.article = article
            review.save()
            messages.success(request, "review sent!")
            return redirect('article-details', pk=pk)

    else:
     form = ReviewForm()
 

    return render(request, "article/reviews.html",
        {
            "article": article,
             "reviews": reviews,
            "review_count": review_count,
            "form": form
        })


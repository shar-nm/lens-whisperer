from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from article.models import Article, Category

# Create your views here.

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)

    return render(request, 'dashboard/dash.html', {
        'articles': articles,
    })
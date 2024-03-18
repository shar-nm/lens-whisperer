from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from article.models import Article

# Create your views here.

@login_required
def index(request):
    articles = Article.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dash.html', {
        'articles': articles,
    })
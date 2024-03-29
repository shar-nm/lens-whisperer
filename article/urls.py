from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='new-article'),
    path('<int:pk>/article-details', views.article_details, name='article-details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('articles/<int:pk>/', views.review_view, name='review'),
]

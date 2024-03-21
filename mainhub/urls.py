from django.urls import path, include

from . import views

urlpatterns = [
    path('article/', include('article.urls')),
    path('', views.mainhub, name='mainhub'),
]
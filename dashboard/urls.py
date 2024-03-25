from django.urls import path, include

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('article/', include('article.urls')),
    path('mainhub/',include('mainhub.urls')),
    path('mainhub/', include('django.contrib.auth.urls')),

]

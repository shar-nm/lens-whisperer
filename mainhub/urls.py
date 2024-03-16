from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from . import views
from .forms import SignupForm


urlpatterns = [
    path('', views.mainhub, name='mainhub'),
    path('article/', include('article.urls')),
    path('signup/', views.signup, name='signup'),
]
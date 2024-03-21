from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from . import views
# from .forms import SignupForm 
# from .forms import LoginForm

urlpatterns = [
    path('article/', include('article.urls')),
    path('', views.mainhub, name='mainhub'),
    path('login_user',views.login_user, name='login'),
    path('logout_user',views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
]
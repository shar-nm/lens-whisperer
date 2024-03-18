from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from . import views
# from .forms import SignupForm 
# from .forms import LoginForm

urlpatterns = [
    path('', views.mainhub, name='mainhub'),
    path('article/', include('article.urls')),
    # path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='mainhub/login.html', authentication_form=LoginForm), name='login'),
]
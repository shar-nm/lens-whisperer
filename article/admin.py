from django.contrib import admin
from .models import Category, Article, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Review)
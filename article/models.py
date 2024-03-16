from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, related_name = "articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_posts")
    image = CloudinaryField('image', default='placeholder')
    camera = models.CharField(max_length=100)
    lens = models.CharField(max_length=100)
    aperture = models.CharField(max_length=100)
    shutter_speed = models.CharField(max_length=100)
    Iso = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



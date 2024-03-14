from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class UserRegister(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_image = CloudinaryField('image', default='placeholder')
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    



from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
     username = models.CharField(max_length=200, default='full name')
     email = models.EmailField(max_length=200)
     password = models.CharField(max_length=200)
     password2 = models.CharField(max_length=200, default='repeat password')    

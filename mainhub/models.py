from django.db import models


class UserRegister(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='full name')
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100, default='repeat password')
    

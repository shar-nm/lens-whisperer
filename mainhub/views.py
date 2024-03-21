from django.shortcuts import render
from django.contrib import messages


def mainhub(request):
    return render(request, 'mainhub/main.html')

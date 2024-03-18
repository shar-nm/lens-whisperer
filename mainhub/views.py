from django.shortcuts import render, redirect
# from .forms import SignupForm
# from .models import User


# Create your views here.


def mainhub(request):
    return render(request, 'mainhub/main.html')




# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('/login/')
#     else:
#         form = SignupForm()
        
#     return render(request, 'mainhub/signup.html', {
#         'form': form
#     })











     
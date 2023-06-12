from django.shortcuts import render

# login
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def login(request):
    return render(request, 'registration/login.html')

def loginout(request):
    logout(request)
    return render(request, 'login/logout.html')

def register(request):
    return render(request, 'login/register.html')
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# login
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def log_in(request):
    return render(request, 'registration/login.html')

def loginout(request):
    logout(request)
    return render(request, 'login/logout.html')

def register(request):
    registration_form = {'form' : UserRegisterForm()}
    if request.method == 'POST':
        registration_form = {'form' : UserRegisterForm(request.POST)}
        if registration_form['form'].is_valid():
            registration_form['form'].save()
            user = authenticate(username=registration_form['form'].cleaned_data['username'], password=registration_form['form'].cleaned_data['password1'])
            login(request, user)
            return render(request, 'login/index.html')
            #return redirect('index')
    return render(request, 'registration/register.html',context=registration_form)
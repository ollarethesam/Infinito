from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import CreateUserForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('menu'))
        else:
            return render(request, 'Login/login.html', {'form_errors': 'Credenziali Errate'})
    else:
        return render(request, 'Login/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'Login/login.html')

def signup(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            pass
    return render(request, 'Login/signup.html',{
        'form': form
    })
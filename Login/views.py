from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

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
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import CreateUserForm
from .models import CustomUser

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

def bg(request):
    if request.method == 'POST':
        print(request.POST)
        user_instance = CustomUser.objects.get(pk=request.user.id)
        if request.POST.get('image') == '1':
            user_instance.bg_image.delete(False)
            user_instance.bg_image = None
        if not request.FILES.get('image') == None:
            user_instance.bg_image.delete(False)
            user_instance.bg_image = request.FILES.get('image')
        if not request.POST.get('color') == '#000000':
            user_instance.bg_color = request.POST.get('color')
        if request.POST.get('resize'):
            user_instance.image_resize = True
            print(user_instance.image_resize)
        else:
            user_instance.image_resize = False
        user_instance.save()
    return JsonResponse({})
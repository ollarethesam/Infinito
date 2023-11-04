from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'DataManager/menu.html')
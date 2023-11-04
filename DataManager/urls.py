from importlib import *
from django.urls import path
from .views.__init__ import __all__
for i in __all__:
    exec(f'from .views.{i} import {i}')

urlpatterns = [
    path('', menu, name='menu'),
    path('Gestione-Tabella-Banche', banche, name='banche')
]
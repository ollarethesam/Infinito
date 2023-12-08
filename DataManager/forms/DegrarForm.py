from DataManager.models.degrar import Degrar
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class DegrarForm(ModelForm):
    class Meta:
        model = Degrar
        fields = ['codgar', 'desgar']
        labels = {
            'codgar': 'Codice',
            'desgar': 'Descrizione',
        }
        widgets = {
            'codgar': forms.TextInput(attrs={'class':'codgar form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desgar': forms.TextInput(attrs={'class':'desgar form-control', 'autocomplete': 'off', 'id': False})
        }
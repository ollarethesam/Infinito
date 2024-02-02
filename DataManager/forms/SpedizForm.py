from DataManager.models.spediz import Spediz
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class SpedizForm(ModelForm):
    class Meta:
        model = Spediz
        fields = ['codspe', 'desspe']
        labels = {
            'codspe': 'Codice Spedizione',
            'desspe': 'Descrizione',
        }
        widgets = {
            'codspe': forms.TextInput(attrs={'class':'codspe Spediz form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desspe': forms.TextInput(attrs={'class':'desspe Spediz form-control', 'autocomplete': 'off', 'id': False})
        }
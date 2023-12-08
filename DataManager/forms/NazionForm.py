from DataManager.models.nazion import Nazion
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class NazionForm(ModelForm):
    class Meta:
        model = Nazion
        fields = ['codnaz', 'desnaz']
        labels = {
            'codnaz': 'Codice Nazione',
            'desnaz': 'Descrizione Nazione',
        }
        widgets = {
            'codnaz': forms.TextInput(attrs={'class':'codnaz form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desnaz': forms.TextInput(attrs={'class':'desnaz form-control', 'autocomplete': 'off', 'id': False})
        }
from DataManager.models.artico import Artico
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class ArticoForm(ModelForm):
    class Meta:
        model = Artico
        fields = ['codart', 'desart', 'prezzo']
        labels = {
            'codart': 'Codice Articolo',
            'desart': 'Descrizione',
            'prezzo': 'Prezzo'
        }
        widgets = {
            'codart': forms.TextInput(attrs={'class':'codart form-control pk medium', 'autocomplete': 'off', 'id': False}),
            'desart': forms.TextInput(attrs={'class':'desart form-control', 'autocomplete': 'off', 'id': False}),
            'prezzo': forms.NumberInput(attrs={'class':'prezzo form-control short', 'autocomplete': 'off', 'step':'0.0001', 'value':'0.0000', 'id': False})
        }
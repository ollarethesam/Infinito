from DataManager.models.porto import Porto
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class PortoForm(ModelForm):
    class Meta:
        model = Porto
        fields = ['codpor', 'despor']
        labels = {
            'codpor': 'Codice Porto',
            'despor': 'Descrizione',
        }
        widgets = {
            'codpor': forms.TextInput(attrs={'class':'codpor Porto form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'despor': forms.TextInput(attrs={'class':'despor Porto form-control', 'autocomplete': 'off', 'id': False})
        }
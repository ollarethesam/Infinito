from DataManager.models.zone import Zone
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class ZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields = ['codzon', 'deszon']
        labels = {
            'codzon': 'Codice Zona',
            'deszon': 'Descrizione Zona',
        }
        widgets = {
            'codzon': forms.TextInput(attrs={'class':'codzon form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'deszon': forms.TextInput(attrs={'class':'deszon form-control', 'autocomplete': 'off', 'id': False})
        }
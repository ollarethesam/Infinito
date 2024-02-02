from DataManager.models.valute import Valute
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class ValuteForm(ModelForm):
    class Meta:
        model = Valute
        fields = ['codval', 'desval', 'simval', 'valcam']
        labels = {
            'codval': 'Codice Valuta',
            'desval': 'Descrizione',
            'simval': 'Simbolo Valuta',
            'valcam': 'Valore Cambio'
        }
        widgets = {
            'codval': forms.TextInput(attrs={'class':'codval Valute form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desval': forms.TextInput(attrs={'class':'desval Valute form-control', 'autocomplete': 'off', 'id': False}),
            'simval': forms.TextInput(attrs={'class':'simval form-control', 'autocomplete': 'off', 'id': False}),
            'valcam': forms.TextInput(attrs={'class':'valcam form-control', 'autocomplete': 'off', 'id': False})
        }
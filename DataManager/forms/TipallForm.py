from DataManager.models.tipall import Tipall
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class TipallForm(ModelForm):
    class Meta:
        model = Tipall
        fields = ['codtal', 'destal']
        labels = {
            'codtal': 'Codice',
            'destal': 'Descrizione',
        }
        widgets = {
            'codtal': forms.TextInput(attrs={'class':'codtal Tipall form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'destal': forms.TextInput(attrs={'class':'destal Tipall form-control', 'autocomplete': 'off', 'id': False}),
        }
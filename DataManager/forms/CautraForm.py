from DataManager.models.cautra import Cautra
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class CautraForm(ModelForm):
    class Meta:
        STAFAT = [
        ("1", "Si"),
        ("0", "No"),
        ]
        model = Cautra
        fields = ['codcau', 'descau', 'stafat']
        labels = {
            'codcau': 'Codice',
            'descau': 'Descrizione',
            'stafat': 'Stampa Fattura',
        }
        widgets = {
            'codcau': forms.TextInput(attrs={'class':'codcau Cautra form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descau': forms.TextInput(attrs={'class':'descau Cautra form-control', 'autocomplete': 'off', 'id': False}),
            'stafat': forms.Select(attrs={'class':'stafat form-control', 'autocomplete': 'off', 'id': False}, choices=STAFAT)
        }
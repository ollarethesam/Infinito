from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.cenlav import Cenlav

class CenlavForm(ModelForm):
    class Meta:
        model = Cenlav
        fields = ['codcen', 'descen']
        labels = {
            'codcen': 'Codice Gruppo',
            'descen': 'Descrizione Gruppo',
        }
        widgets = {
            'codcen': forms.TextInput(attrs={'class':'codcen form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descen': forms.TextInput(attrs={'class':'descen form-control', 'autocomplete': 'off', 'id': False}),
        }
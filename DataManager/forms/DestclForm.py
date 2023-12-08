from DataManager.models.destcl import Destcl
from django import forms
from django.forms import ModelForm

class DestclForm(ModelForm):
    ragsoc = forms.CharField(label='Ragione Sociale', widget=forms.TextInput(attrs={'class':'ragsoc form-control', 'readonly': True, 'id': False}))
    class Meta:
        model = Destcl
        fields = ['codest', 'dedest', 'codcli', 'ragsoc']
        labels = {
            'codest': 'Codice Destinatario',
            'dedest': 'Descrizione',
            'codcli': 'Codice Cliente',
        }
        widgets = {
            'codest': forms.TextInput(attrs={'class':'codest form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'dedest': forms.TextInput(attrs={'class':'dedest form-control', 'autocomplete': 'off', 'id': False}),
            'codcli': forms.TextInput(attrs={'class':'codcli form-control fk', 'autocomplete': 'off', 'id': False}),
        }
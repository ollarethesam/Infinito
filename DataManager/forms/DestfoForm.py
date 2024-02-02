from django import forms
from DataManager.models.destfo import Destfo


class DestfoForm(forms.ModelForm):
    ragsoc = forms.CharField(label='Ragione Sociale', widget=forms.TextInput(attrs={'class':'ragsoc Fornit form-control', 'readonly': True, 'id': False}))
    class Meta:
        model = Destfo
        fields = ['codest', 'dedest','codfor', 'ragsoc']
        labels = {
            'codfor': 'Codice Fornitore',
            'codest': 'Codice Destinatario',
            'dedest': 'Descrizione Destinatario'
        }
        widgets = {
            'codfor': forms.TextInput(attrs={'class':'codfor Fornit form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'codest': forms.TextInput(attrs={'class':'codest Destfo form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'dedest': forms.TextInput(attrs={'class':'dedest Destfo form-control', 'autocomplete': 'off', 'id': False}),
        }

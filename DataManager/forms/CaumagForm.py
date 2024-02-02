from DataManager.models.caumag import Caumag
from django import forms
from django.forms import ModelForm

class CaumagForm(ModelForm):
    class Meta:
        AZIONE = [
            ('C', 'Carico'),
            ('S', 'Scarico'),
            ('N', 'Nulla')
        ]
        model = Caumag
        fields = ['codcau', 'descau', 'abbrev', 'azione']
        labels = {
            'codcau':'Codice',
            'descau':'Descrizione',
            'abbrev':'Abbreviazione',
            'azione':'Azione'
        }
        widgets = {
            'codcau': forms.TextInput(attrs={'class':'codcau Caumag form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descau': forms.TextInput(attrs={'class':'descau Caumag form-control', 'autocomplete': 'off', 'id': False}),
            'abbrev': forms.TextInput(attrs={'class':'stafat form-control', 'autocomplete': 'off', 'id': False}),
            'azione': forms.Select(attrs={'class':'stafat form-control', 'autocomplete': 'off', 'id': False}, choices=AZIONE)
        }
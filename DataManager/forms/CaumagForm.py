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
        APPART = [
            ('F', 'Fornitori'),
            ('C', 'Clienti'),
            ('P', 'Produzione'),
            ('N', 'Nessuna')
        ]
        model = Caumag
        fields = ['codcau', 'descau', 'abbrev', 'azione', 'appart', 'valori', 'gesord']
        labels = {
            'codcau':'Codice',
            'descau':'Descrizione',
            'abbrev':'Abbreviazione',
            'azione':'Azione',
            'appart': 'Appartenenza',
            'valori': 'Valorizza',
            'gesord': 'Gestione Ordini'
        }
        widgets = {
            'codcau': forms.TextInput(attrs={'class':'codcau Caumag form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descau': forms.TextInput(attrs={'class':'descau Caumag form-control l35', 'autocomplete': 'off', 'id': False}),
            'abbrev': forms.TextInput(attrs={'class':'abbrev form-control', 'autocomplete': 'off', 'id': False}),
            'azione': forms.Select(attrs={'class':'azione form-control l9', 'autocomplete': 'off', 'id': False}, choices=AZIONE),
            'appart': forms.Select(attrs={'class':'appart form-control l9', 'autocomplete': 'off', 'id': False}, choices=APPART),
            'valori': forms.CheckboxInput(attrs={'class':'valori form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'gesord': forms.CheckboxInput(attrs={'class':'gesord form-control checkbox', 'autocomplete': 'off', 'id': False})
        }
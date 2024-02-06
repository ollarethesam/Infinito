from DataManager.models.movmag import Movmag
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class MovmagForm(ModelForm):
    nuorfo = forms.CharField(required = False,label='Numero Ordine', widget=forms.TextInput(attrs={'class':'nuorfo Ordfor form-control', 'readonly': True, 'id': False}))
    anorfo = forms.CharField(required = False,label='Anno Ordine', widget=forms.TextInput(attrs={'class':'anorfo Ordfor form-control', 'readonly': True, 'id': False}))
    nuorcl = forms.CharField(required = False,label='Numero Ordine', widget=forms.TextInput(attrs={'class':'nuorcl Ordcli form-control', 'readonly': True, 'id': False}))
    anorcl = forms.CharField(required = False,label='Anno Ordine', widget=forms.TextInput(attrs={'class':'anorcl Ordcli form-control', 'readonly': True, 'id': False}))
    nuorpr = forms.CharField(required = False,label='Numero Ordine', widget=forms.TextInput(attrs={'class':'nuorpr Ordpro form-control', 'readonly': True, 'id': False}))
    anorpr = forms.CharField(required = False,label='Anno Ordine', widget=forms.TextInput(attrs={'class':'anorpr Ordpro form-control', 'readonly': True, 'id': False}))
    class Meta:
        ORDSAL = [
            ('S', 'Saldo'),
            ('A', 'Acconto'),
        ]
        model = Movmag
        fields = [
            'anno', 'numpro', 'datmov', 'numdoc', 'codart', 'codcau',
            'quanti', 'prezzo', 'valore', 'codcli', 'codfor',
            'note', 'quamod', 'nuorfo', 'anorfo', 'nuorcl', 'anorcl', 'nuorpr', 'anorpr',
            'quakg', 'ordsal', 'numddt', 'annddt',
            'codco1', 'codco2', 'codco3', 'codco4', 'codco5', 'quaco1',
            'quaco2', 'quaco3', 'quaco4', 'quaco5'
        ]
        labels = {
            'numpro': 'Numero Progressivo',
            'datmov': 'Data Movimento',
            'anno'  : 'Anno',
            'numdoc': 'Numero Documento',
            'codart': 'Codice Articolo',
            'codcau': 'Codice Causale',
            'quanti': 'Quantità',
            'prezzo': 'Prezzo',
            'valore': 'Valore',
            'codcli': 'Codice Cliente',
            'codfor': 'Codice Fornitore',
            'nuorfo': 'Numero Ordine',
            'nuorcl': 'Numero Ordine',
            'anorfo': 'Anno',
            'anorcl': 'Anno',
            'nuorpr': 'Numero Ordine',
            'anorpr': 'Anno',
            'note'  : 'Note',
            'quamod': 'Quantità Modula',
            'quakg': 'Quantità in Kg',
            'ordsal': 'Saldo/Acconto',
            'numddt': 'Numero DDT',
            'annddt': 'Anno DDT',
            'codco1': 'Codice Commessa',
            'codco2': '',
            'codco3': '',
            'codco4': '',
            'codco5': '',
            'quaco1': 'Quantità',
            'quaco2': '',
            'quaco3': '',
            'quaco4': '',
            'quaco5': '',
        }
        widgets = {
        'numpro': forms.TextInput(attrs={'class': 'numpro form-control l15', 'autocomplete': 'off', 'id': False}),
        'datmov': forms.DateInput(attrs={'class': 'datmov form-control', 'autocomplete': 'off', 'id': False}),
        'anno': forms.TextInput(attrs={'class': 'anno form-control l4', 'autocomplete': 'off', 'id': False}),
        'numdoc': forms.TextInput(attrs={'class': 'numdoc form-control l15', 'autocomplete': 'off', 'id': False}),
        'codart': forms.TextInput(attrs={'class': 'codart form-control', 'autocomplete': 'off', 'id': False}),
        'codcau': forms.TextInput(attrs={'class': 'codcau form-control', 'autocomplete': 'off', 'id': False}),
        'quanti': forms.TextInput(attrs={'class': 'quanti form-control l13', 'autocomplete': 'off', 'id': False}),
        'prezzo': forms.TextInput(attrs={'class': 'prezzo form-control l13', 'autocomplete': 'off', 'id': False}),
        'valore': forms.TextInput(attrs={'class': 'valore form-control l13', 'autocomplete': 'off', 'id': False}),
        'codcli': forms.TextInput(attrs={'class': 'codcli form-control', 'autocomplete': 'off', 'id': False}),
        'codfor': forms.TextInput(attrs={'class': 'codfor form-control', 'autocomplete': 'off', 'id': False}),
        'nuorfo': forms.TextInput(attrs={'class': 'nuorfo form-control', 'autocomplete': 'off', 'id': False}),
        'nuorcl': forms.TextInput(attrs={'class': 'nuorcl form-control', 'autocomplete': 'off', 'id': False}),
        'anorfo': forms.TextInput(attrs={'class': 'anorfo form-control', 'autocomplete': 'off', 'id': False}),
        'anorcl': forms.TextInput(attrs={'class': 'anorcl form-control', 'autocomplete': 'off', 'id': False}),
        'note': forms.TextInput(attrs={'class': 'note form-control l50', 'autocomplete': 'off', 'id': False}),
        'quamod': forms.TextInput(attrs={'class': 'quamod form-control l13', 'autocomplete': 'off', 'id': False}),
        'modula': forms.CheckboxInput(attrs={'class': 'modula from-control checkbox', 'autocomplete': 'off', 'id': False}),
        'quakg': forms.TextInput(attrs={'class': 'quakg form-control l13', 'autocomplete': 'off', 'id': False}),
        'ordsal': forms.Select(attrs={'class': 'ordsal form-control', 'autocomplete': 'off', 'id': False}, choices=ORDSAL),
        'numddt': forms.TextInput(attrs={'class': 'numddt form-control', 'autocomplete': 'off', 'id': False}),
        'annddt': forms.TextInput(attrs={'class': 'annddt form-control', 'autocomplete': 'off', 'id': False}),
        'codco1': forms.TextInput(attrs={'class': 'codco1 form-control', 'autocomplete': 'off', 'id': False}),
        'codco2': forms.TextInput(attrs={'class': 'codco2 form-control', 'autocomplete': 'off', 'id': False}),
        'codco3': forms.TextInput(attrs={'class': 'codco3 form-control', 'autocomplete': 'off', 'id': False}),
        'codco4': forms.TextInput(attrs={'class': 'codco4 form-control', 'autocomplete': 'off', 'id': False}),
        'codco5': forms.TextInput(attrs={'class': 'codco5 form-control', 'autocomplete': 'off', 'id': False}),
        'quaco1': forms.TextInput(attrs={'class': 'quaco1 form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco2': forms.TextInput(attrs={'class': 'quaco2 form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco3': forms.TextInput(attrs={'class': 'quaco3 form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco4': forms.TextInput(attrs={'class': 'quaco4 form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco5': forms.TextInput(attrs={'class': 'quaco5 form-control l13', 'autocomplete': 'off', 'id': False}),
    }
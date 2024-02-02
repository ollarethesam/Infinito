from DataManager.models.movmag import Movmag
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class MovmagForm(ModelForm):
    class Meta:
        ORDSAL = [
            ('S', 'Saldo'),
            ('A', 'Acconto'),
        ]
        model = Movmag
        fields = [
            'anno', 'numpro', 'datmov', 'numdoc', 'codart', 'codcau',
            'quanti', 'prezzo', 'valore', 'codcli', 'codfor',
            'idorfo', 'idorcl','idorpr', 'note', 'quamod',
            'matric', 'quakg', 'ordsal', 'numddt', 'annddt',
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
        'numpro': forms.TextInput(attrs={'class': 'form-control l15', 'autocomplete': 'off', 'id': False}),
        'datmov': forms.DateInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'anno': forms.TextInput(attrs={'class': 'form-control l4', 'autocomplete': 'off', 'id': False}),
        'numdoc': forms.TextInput(attrs={'class': 'form-control l15', 'autocomplete': 'off', 'id': False}),
        'codart': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codcau': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'quanti': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'prezzo': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'valore': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'codcli': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codfor': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'nuorfo': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'nuorcl': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'anorfo': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'anorcl': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'note': forms.TextInput(attrs={'class': 'form-control l50', 'autocomplete': 'off', 'id': False}),
        'quamod': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'modula': forms.CheckboxInput(attrs={'class': 'from-control checkbox', 'autocomplete': 'off', 'id': False}),
        'quakg': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'ordsal': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}, choices=ORDSAL),
        'numddt': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'annddt': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codco1': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codco2': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codco3': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codco4': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'codco5': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': False}),
        'quaco1': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco2': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco3': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco4': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
        'quaco5': forms.TextInput(attrs={'class': 'form-control l13', 'autocomplete': 'off', 'id': False}),
    }
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.dipend import Dipend

class DipendForm(ModelForm):
    class Meta:
        ASSUNT = [
        ("SI", "Si"),
        ("NO", "No"),
        ]
        TIPTAR = [
        ("tj", "Tecnico Junior"),
        ("te", "Tecnico Esperto"),
        ("i", "Ingegnere"),
        ]
        model = Dipend
        fields = ['coddip', 'nome', 'assunt', 'tiptar']
        labels = {
            'coddip': 'Codice Dipendente',
            'nome':   'Nome',
            'assunt': 'Assunto',
            'tiptar': 'Tipo Tariffa',
        }
        widgets = {
            'coddip': forms.TextInput(attrs={'class':'coddip Dipend form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'nome':   forms.TextInput(attrs={'class':'nome Dipend form-control long', 'autocomplete': 'off', 'id': False}),
            'assunt': forms.Select(attrs={'class':'assunt form-control', 'autocomplete': 'off', 'id': False}, choices=ASSUNT),
            'tiptar': forms.Select(attrs={'class':'tiptar form-control', 'autocomplete': 'off', 'id': False}, choices=TIPTAR),
        }
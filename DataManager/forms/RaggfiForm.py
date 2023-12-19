from DataManager.models.raggfi import Raggfi
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class RaggfiForm(ModelForm):
    class Meta:
        model = Raggfi
        fields = ['codrag', 'desrag']
        labels = {
            'codrag': 'Codice',
            'desrag': 'Descrizione',
        }
        widgets = {
            'codrag': forms.TextInput(attrs={'class':'codrag form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desrag': forms.TextInput(attrs={'class':'desrag form-control', 'autocomplete': 'off', 'id': False}),
        }
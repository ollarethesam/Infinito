from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.eseiva import Eseiva

class EseivaForm(ModelForm):
    class Meta:
        model = Eseiva
        fields = ['codese', 'riccli', 'datric']
        labels = {
            'codese': 'Codice Esenzione',
            'riccli': 'Richiesta del CLiente n.',
            'datric': 'Data Richiesta',
        }
        widgets = {
            'codese': forms.TextInput(attrs={'class':'codese form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'riccli': forms.TextInput(attrs={'class':'riccli form-control l3', 'autocomplete': 'off', 'id': False}),
            'datric': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datric form-control l9', 'autocomplete': 'off', 'id': False}),
        }
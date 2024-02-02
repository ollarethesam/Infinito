from DataManager.models.agenti import Agenti
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class AgentiForm(ModelForm):
    class Meta:
        model = Agenti
        fields = ['codage', 'desage', 'provvi']
        labels = {
            'codage': 'Codice Agente',
            'desage': 'Descrizione',
            'provvi': 'Provvigione %'
        }
        widgets = {
            'codage': forms.TextInput(attrs={'class':'codage Agenti form-control pk l3', 'autocomplete': 'off'}),
            'desage': forms.TextInput(attrs={'class':'desage Agenti form-control', 'autocomplete': 'off'}),
            'provvi': forms.NumberInput(attrs={'class':'provvi form-control short', 'autocomplete': 'off', 'min': '0.01', 'max':'100.00', 'step':'0.01', 'value':'0.00'})
        }
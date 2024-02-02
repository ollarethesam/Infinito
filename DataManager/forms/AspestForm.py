from DataManager.models.aspest import Aspest
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class AspestForm(ModelForm):
    class Meta:
        model = Aspest
        fields = ['codasp', 'desasp']
        labels = {
            'codasp': 'Codice',
            'desasp': 'Descrizione',
        }
        widgets = {
            'codasp': forms.TextInput(attrs={'class':'codasp Aspest form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desasp': forms.TextInput(attrs={'class':'desasp Aspest form-control', 'autocomplete': 'off', 'id': False}),
        }
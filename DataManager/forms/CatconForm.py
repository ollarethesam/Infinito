from DataManager.models.catcon import Catcon
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class CatconForm(ModelForm):
    despia = forms.CharField(label='Descrizione Conto', widget=forms.TextInput(attrs={'class':'despia form-control', 'autocomplete': 'off', 'id': False}))
    class Meta:
        model = Catcon
        fields = ['codcat', 'descat', 'codpia', 'despia']
        labels = {
            'codcat': 'Codice',
            'descat': 'Descrizione',
            'codpia': 'Codice Conto',
        }
        widgets = {
            'codcat': forms.TextInput(attrs={'class':'codcat form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descat': forms.TextInput(attrs={'class':'descat form-control', 'autocomplete': 'off', 'id': False}),
            'codpia': forms.TextInput(attrs={'class':'codpia form-control l6', 'autocomplete': 'off', 'id': False})
        }
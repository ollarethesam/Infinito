from DataManager.models.ivacor import Ivacor
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class IvacorForm(ModelForm):
    class Meta:
        NATURA = [
        ("01", "Escluso Articolo 15"),
        ("02", "numeor 2"),
        ("03", "numero 3"),
        ]
        model = Ivacor
        fields = ["codiva", "desiva", "aliquo", "natura", "esclip"]
        labels = {
            'codiva': 'Codice IVA',
            'desiva': 'Descrizione IVA',
            'aliquo': 'Aliquota',
            'natura': 'Natura',
            'esclip': 'Escluso da Lipe',
        }
        widgets = {
            'codiva': forms.TextInput(attrs={'class':'codiva form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desiva': forms.TextInput(attrs={'class':'desiva form-control', 'autocomplete': 'off', 'id': False}),
            'aliquo': forms.TextInput(attrs={'class':'aliquo form-control', 'autocomplete': 'off', 'id': False}),
            'natura': forms.Select(attrs={'class':'natura form-control', 'autocomplete': 'off', 'id': False}, choices=NATURA),
            'esclip': forms.CheckboxInput(attrs={'class':'esclip form-control checkbox', 'autocomplete': 'off', 'id': False})
        }
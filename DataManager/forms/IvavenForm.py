from DataManager.models.ivaven import Ivaven
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class IvavenForm(ModelForm):
    class Meta:
        INDAGG = [
        ("1", "Imponibile"),
        ("2", "Non Imponibile"),
        ("3", "Esente"),
        ("4", "Imponibile con IVA non Esposta in Fattura"),
        ("5", "Intracomunitario"),
        ("6", "Nessuno"),
        ]
        NATURA = [
        ("01", "Escluso Articolo 15"),
        ("02", "numeor 2"),
        ("03", "numero 3"),
        ]
        model = Ivaven
        fields = ["codiva", "desiva", "aliquo", "indagg", "natura", "esclip"]
        labels = {
            'codiva': 'Codice IVA',
            'desiva': 'Descrizione IVA',
            'aliquo': 'Aliquota',
            'indagg': 'ind. Aggior.',
            'natura': 'Natura',
            'esclip': 'Escluso da Lipe',
        }
        widgets = {
            'codiva': forms.TextInput(attrs={'class':'codiva Ivaven form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desiva': forms.TextInput(attrs={'class':'desiva Ivaven form-control', 'autocomplete': 'off', 'id': False}),
            'aliquo': forms.TextInput(attrs={'class':'aliquo form-control', 'autocomplete': 'off', 'id': False}),
            'indagg': forms.Select(attrs={'class':'indagg form-control', 'autocomplete': 'off', 'id': False}, choices=INDAGG),
            'natura': forms.Select(attrs={'class':'natura form-control', 'autocomplete': 'off', 'id': False}, choices=NATURA),
            'esclip': forms.CheckboxInput(attrs={'class':'esclip form-control checkbox', 'autocomplete': 'off', 'id': False})
        }
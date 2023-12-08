from DataManager.models.ivaacq import Ivaacq
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class IvaacqForm(ModelForm):
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
        model = Ivaacq
        fields = ['codiva', 'desiva', 'aliquo', 'indetr', 'indagg', 'natura', 'esclip']
        labels = {
            'codiva': 'Codice IVA',
            'desiva': 'Descrizione IVA',
            'aliquo': 'Aliquota',
            'indetr': 'Indetraibilità',
            'indagg': 'ind. Aggior.',
            'natura': 'Natura',
            'esclip': 'Escluso da Lipe',
        }
        widgets = {
            'codiva': forms.TextInput(attrs={'codiva class':'form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'desiva': forms.TextInput(attrs={'desiva class':'form-control', 'autocomplete': 'off', 'id': False}),
            'aliquo': forms.TextInput(attrs={'aliquo class':'form-control', 'autocomplete': 'off', 'id': False}),
            'indetr': forms.TextInput(attrs={'indetr class':'form-control', 'autocomplete': 'off', 'id': False}),
            'indagg': forms.Select(attrs={'indagg class':'form-control', 'autocomplete': 'off', 'id': False}, choices=INDAGG),
            'natura': forms.Select(attrs={'natura class':'form-control', 'autocomplete': 'off', 'id': False}, choices=NATURA),
            'esclip': forms.CheckboxInput(attrs={'esclip class':'form-control checkbox', 'autocomplete': 'off', 'id': False})
        }
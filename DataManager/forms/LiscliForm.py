from django import forms
from DataManager.models.liscli import Liscli


class LiscliForm(forms.ModelForm):
    ragsoc = forms.CharField(label='Ragione Sociale', widget=forms.TextInput(attrs={'class':'ragsoc form-control', 'readonly': True, 'id': False}))
    desart = forms.CharField(label='Descrizione Articolo', widget=forms.TextInput(attrs={'class':'desart form-control', 'readonly': True, 'id': False}))
    class Meta:
        model = Liscli
        fields = ['codcli', 'ragsoc', 'codart', 'desart', 'prezzo']
        field_order = ['codcli', 'ragsoc', 'codart', 'desart', 'prezzo']
        labels = {
            'codcli': 'Codice Cliente',
            'codart': 'Codice Articolo',
            'prezzo': 'prezzo'
        }
        widgets = {
            'codcli': forms.TextInput(attrs={'class':'codcli form-control pk l3 main', 'autocomplete': 'off', 'id': False}),
            'codart': forms.TextInput(attrs={'class':'codart form-control pk medium', 'autocomplete': 'off', 'id': False}),
            'desart': forms.TextInput(attrs={'class':'desart form-control', 'autocomplete': 'off', 'id': False}),
            'prezzo': forms.NumberInput(attrs={'class':'prezzo form-control long', 'autocomplete': 'off', 'step':'0.0001', 'id': False})
        }

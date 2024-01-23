from DataManager.models.banche import Banche
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class BancheForm(ModelForm):
    class Meta:
        model = Banche
        fields = ['codban', 'desban', 'codabi', 'codcab', 'codsia', 'iban', 'bic']
        labels = {
            'codban': 'Codice Banca',
            'desban': 'Descrizione Banca',
            'codabi': 'Codice ABI',
            'codcab': 'Codice CAB',
            'codsia': 'Codice SIA',
            'iban':   'IBAN',
            'bic':    'BIC',
        }
        widgets = {
            'codban': forms.TextInput(attrs={'class':'codban form-control l3 pk', 'autocomplete': 'off', 'id': False}),
            'desban': forms.TextInput(attrs={'class':'desban form-control l30', 'autocomplete': 'off', 'id': False}),
            'codabi': forms.TextInput(attrs={'class':'codabi form-control l5', 'autocomplete': 'off', 'id': False}),
            'codcab': forms.TextInput(attrs={'class':'codcab form-control l5', 'autocomplete': 'off', 'id': False}),
            'codsia': forms.TextInput(attrs={'class':'codsia form-control l5', 'autocomplete': 'off', 'id': False}),
            'iban':   forms.TextInput(attrs={'class':'iban form-control l27', 'autocomplete': 'off', 'id': False}),
            'bic':    forms.TextInput(attrs={'class':'bic form-control l11', 'autocomplete': 'off', 'id': False}),
        }
    def clean_codabi(self, *args, **kwargs):
        codabi = self.cleaned_data.get('codabi')
        if len(codabi) != 5:
            raise forms.ValidationError("il codice ABI deve essere lungo 5 caratteri")
        else:
            return codabi
    def clean_codcab(self, *args, **kwargs):
        codcab = self.cleaned_data.get('codcab')
        if len(codcab) != 5:
            raise forms.ValidationError("il codice CAB deve essere lungo 5 caratteri")
        else:
            return codcab
    def clean_codsia(self, *args, **kwargs):
        codsia = self.cleaned_data.get('codsia')
        if len(codsia) != 5:
            raise forms.ValidationError("il codice SIA deve essere lungo 5 caratteri")
        else:
            return codsia
    def clean_iban(self, *args, **kwargs):
        iban = self.cleaned_data.get('iban')
        if len(iban) != 27:
            raise forms.ValidationError("L'iban deve essere lungo 27 caratteri")
        else:
            return iban
    def clean_bic(self, *args, **kwargs):
        bic = self.cleaned_data.get('bic')
        if len(bic) != 11:
            raise forms.ValidationError("il codice BIC deve essere lungo 11 caratteri")
        else:
            return bic
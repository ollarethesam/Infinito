from DataManager.models.piacon import Piacon
from DataManager.models.conabi import Conabi
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
import re

class PiaconForm(ModelForm):
    decoab = forms.BooleanField(required = False,label='Rimuovi Con. Abituale', widget=forms.CheckboxInput(attrs={'class':'decoab form-control checkbox', 'autocomplete': 'off', 'id': False}))
    codcon = forms.CharField(required = False,label='Contropartia Abituale', widget=forms.TextInput(attrs={'class':'codcon form-control l9', 'autocomplete': 'off', 'readonly': True, 'id': False}))
    descon = forms.CharField(required = False,label='Descrizione', widget=forms.TextInput(attrs={'class':'descon form-control l30', 'autocomplete': 'off', 'readonly': True, 'id': False}))
    class Meta:
        model = Piacon
        fields = ['codpia', 'despia', 'codcon', 'descon', 'decoab']
        labels = {
            'codpia': 'Codice Conto',
            'despia': 'Descrizione',
        }
        widgets = {
            'codpia': forms.TextInput(attrs={'class':'codpia form-control pk l9', 'autocomplete': 'off', 'id': False}),
            'despia': forms.TextInput(attrs={'class':'despia form-control l30', 'autocomplete': 'off', 'id': False}),
        }
    
    def clean_codpia(self):
        codpia = self.cleaned_data.get('codpia')
        # Check if codpia starts with a number between 1 and 4
        if not re.match(r'^[1-4]', codpia):
            raise forms.ValidationError("Il codice conto deve iniziare con un numero tra 1 e 4")
        # Check if codpia ends in at least 5 consecutive numbers
        if not re.search(r'\d{5,}$', codpia):
            raise forms.ValidationError("il codice conto deve finire con 5 numeri consecutivi")
        if not(codpia.endswith('00000')):
                print(f'{codpia[4:]}00000')
                if Piacon.objects.filter(pk=f'{codpia[:4]}00000').exists():
                    return codpia
                else:
                    raise forms.ValidationError("il codice conto non ha un mastro")
        else:
            return codpia
    
    def clean_codcon(self):
        codcon = self.cleaned_data.get('codcon')
        codpia = self.cleaned_data.get('codpia')
        if codcon:
            codcon = Conabi.objects.get(pk=codcon)
            return codcon
from DataManager.models.catego import Catego
from django import forms
from django.forms import ModelForm

class CategoForm(ModelForm):
    class Meta:
        model = Catego
        fields = ['codcat', 'descat']
        labels = {
            'codcat': 'Codice Categoria',
            'descat': 'Descrizione Categoria',
        }
        widgets = {
            'codcat': forms.TextInput(attrs={'class':'codcat form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'descat': forms.TextInput(attrs={'class':'descat form-control', 'autocomplete': 'off', 'id': False})
        }
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.scacli import Scacli

class ScacliForm(ModelForm):
    class Meta:
        TIPPAG = [
        ("B", "Bonifico Bancario"),
        ("D", "Diretto"),
        ("P", "Pareggio Partita"),
        ("R", "Ricevuta Bancaria"),
        ("T", "Tratta"),
        ]
        
        model = Scacli
        fields = ["numpro", "codcli", "tipdoc", "datdoc", "numfat", "descri", "impfat", "imppag", "codval", "codpag", "cambio", "datsca", "pagato", "codban", "tippag"]
        labels = {
            'codpag': 'Codice',
            'despag': 'Descrizione',
            'tippag': 'Tipo Pagamento',
            'numrat': 'Numero Rate',
            'giosca': 'gg. x Part. Scadenza',
            'period': 'Periodicità',
            'tipsca': 'Tipo Scadenza',
            'escmes': 'Esclusione Mesi',
            'scocas': 'Sconto Pronta Cassa',
            'gifisc': 'Giorno Fisso Scadenza',
            'modpag': 'Modalità Pagamento',
        }
        widgets = {
            'codpag': forms.TextInput(attrs={'class':'codpag form-control pk l3', 'autocomplete': 'off', 'id': False}),
            'despag': forms.TextInput(attrs={'class':'despag form-control', 'autocomplete': 'off', 'id': False}),
            'tippag': forms.Select(attrs={'class':'tippag form-control', 'autocomplete': 'off', 'id': False}, choices=TIPPAG),
            'numrat': forms.NumberInput(attrs={'class':'numrat form-control', 'autocomplete': 'off', 'id': False}),
            'giosca': forms.NumberInput(attrs={'class':'giosca form-control', 'autocomplete': 'off', 'id': False}),
            'period': forms.NumberInput(attrs={'class':'period form-control', 'autocomplete': 'off', 'id': False}),
            'tipsca': forms.Select(attrs={'class':'tipsca form-control', 'autocomplete': 'off', 'id': False}),
            'escmes': forms.Select(attrs={'class':'escmes form-control', 'autocomplete': 'off', 'id': False}),
            'scocas': forms.NumberInput(attrs={'class':'scocas form-control', 'autocomplete': 'off', 'id': False}),
            'gifisc': forms.NumberInput(attrs={'class':'gifisc form-control', 'autocomplete': 'off', 'id': False}),
            'modpag': forms.Select(attrs={'class':'modpag form-control', 'autocomplete': 'off', 'id': False}),
        }
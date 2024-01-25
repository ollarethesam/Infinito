from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.scacli import Scacli

class ScacliForm(ModelForm):
    ragsoc = forms.CharField(required=False, label='Ragione Sociale', widget=forms.TextInput(attrs={'class':'ragsoc form-control', 'id': False}))
    desval = forms.CharField(required=False, label='Descrizione', widget=forms.TextInput(attrs={'class':'desval form-control', 'id': False}))
    despag = forms.CharField(required=False, label='Descrizione', widget=forms.TextInput(attrs={'class':'despag form-control', 'id': False}))
    desban = forms.CharField(required=False, label='Descrizione', widget=forms.TextInput(attrs={'class':'desban form-control', 'id': False}))

    class Meta:
        TIPPAG = [
            ("B", "Bonifico Bancario"),
            ("D", "Diretto"),
            ("P", "Pareggio Partita"),
            ("R", "Ricevuta Bancaria"),
            ("T", "Tratta"),
        ]
        PAGATO = [
            ('S', 'Si'),
            ('N', 'No'),
            ('I', 'Insoluto')
        ]
        TIPDOC = [
            ('F', 'Fattura'),
            ('N', 'Nota Credito')
        ]
        model = Scacli
        fields = ["numpro", "codcli", 'ragsoc', "tipdoc", "datdoc", "numfat", "descri", "impfat", "imppag", "codval", 'desval', "codpag", 'despag', "cambio", "datsca", "pagato", "codban", 'desban', "tippag"]
        labels = {
            'numpro': 'Numero Progressivo',
            'codcli': 'Codice Cliente',
            'tipdoc': 'Tipo Documento',
            'datdoc': 'Data Documento',
            'numfat': 'Numero Fattura',
            'descri': 'Descrizione',
            'impfat': 'Importo Fattura',
            'imppag': 'Importo da Pagare',
            'codval': 'Codice Valuta',
            'codpag': 'Codice Pagamento',
            'cambio': 'Cambio',
            'datsca': 'Data Scadenza',
            'pagato': 'Pagato',
            'codban': 'Codice Banca',
            'tippag': 'Tipo Pagamento',
        }
        widgets = {
            'numpro': forms.TextInput(attrs={'class':'numpro form-control pk l7', 'autocomplete': 'off', 'id': False}),
            'codcli': forms.TextInput(attrs={'class':'codcli form-control l5', 'autocomplete': 'off', 'id': False}),
            'tipdoc': forms.Select(attrs={'class':'tipdoc form-control l9', 'autocomplete': 'off', 'id': False}, choices=TIPDOC),
            'datdoc': forms.DateInput(format='%d-%m', attrs={'class':'datdoc form-control', 'autocomplete': 'off', 'id': False}),
            'numfat': forms.NumberInput(attrs={'class':'numfat form-control l5', 'autocomplete': 'off', 'id': False}),
            'descri': forms.TextInput(attrs={'class':'descri form-control l35', 'autocomplete': 'off', 'id': False}),
            'impfat': forms.NumberInput(attrs={'class':'impfat form-control l13', 'autocomplete': 'off', 'id': False}),
            'imppag': forms.NumberInput(attrs={'class':'imppag form-control l13', 'autocomplete': 'off', 'id': False}),
            'codval': forms.TextInput(attrs={'class':'codval form-control l3', 'autocomplete': 'off', 'id': False}),
            'codpag': forms.TextInput(attrs={'class':'codpag form-control l4', 'autocomplete': 'off', 'id': False}),
            'cambio': forms.NumberInput(attrs={'class':'cambio form-control l11', 'autocomplete': 'off', 'id': False}),
            'datsca': forms.DateInput(format='%d-%m', attrs={'class':'datsca form-control l35', 'autocomplete': 'off', 'id': False}),
            'pagato': forms.Select(attrs={'class':'pagato form-control l7', 'autocomplete': 'off', 'id': False}, choices=PAGATO),
            'codban': forms.TextInput(attrs={'class':'codban form-control l3', 'autocomplete': 'off', 'id': False}),
            'tippag': forms.Select(attrs={'class':'tippag form-control l18', 'autocomplete': 'off', 'id': False}, choices=TIPPAG),
        }
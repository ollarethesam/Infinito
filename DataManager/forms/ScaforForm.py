from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.scafor import Scafor

class ScaforForm(ModelForm):
    ragsoc = forms.CharField(required=False, label='Ragione Sociale', widget=forms.TextInput(attrs={'class':'ragsoc form-control', 'id': False}))
    desval = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'class':'desval form-control', 'id': False}))
    despag = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'class':'despag form-control', 'id': False}))
    desban = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'class':'desban form-control', 'id': False}))

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
        MODPAG = [
            ('', ''),
            ("MP01", "MP01-Contanti"),
            ("MP02", "MP02-Assengno"),
            ("MP03", "MP03-Assengno Circolare"),
            ("MP04", "MP04-Contanti Presso Tesoreria"),
            ("MP05", "MP05-Bonifico"),
            ("MP06", "MP06-Valigia Cambiario"),
            ("MP07", "MP07-Bollettino Bancario"),
            ("MP08", "MP08-Carta Di Pagamento"),
            ("MP09", "MP09-RID"),
            ("MP10", "MP10-RID Utente"),
            ("MP11", "MP11-RID Veloce"),
            ("MP12", "MP12-RIBA"),
            ("MP13", "MP13-MAV"),
            ("MP14", "MP14-Quietanza Erario"),
            ("MP15", "MP15-Giroconto su COnti di Contabilità Speciale"),
            ("MP16", "MP16-Domiciliazione Bancaria"),
            ("MP17", "MP17-Domiciliazione Postale"),
            ("MP18", "MP18-Bollettino di C/C Postale"),
            ("MP19", "MP19-SEPA Direct Debit"),
            ("MP20", "MP20-SEPA Direct Debit Core"),
            ("MP21", "MP21-SEPA Direct Debit B2B"),
            ("MP22", "MP22-Trattenuta su Somme Già Riscosse"),
        ]
        model = Scafor
        fields = ["numpro", 'descri', "codfor", 'ragsoc', "tipdoc", "datdoc", 'protoc', "numfat", "impfat", "imppag", "codval", 'desval', "codpag", 'despag', "cambio", "datsca", "pagato", "codban", 'desban', "tippag", 'modpag']
        labels = {
            'numpro': 'Numero Progressivo',
            'codfor': 'Codice Fornitore',
            'tipdoc': 'Tipo Documento',
            'datdoc': 'Data Documento',
            'protoc': 'Numero Protocollo',
            'numfat': 'Numero Fattura',
            'descri': 'Descrizione',
            'impfat': 'Importo Fattura',
            'imppag': 'Importo da Pagare',
            'codval': 'Codice Valuta',
            'codpag': 'Codice Pagamento',
            'modpag': 'Modalità Pagamento',
            'cambio': 'Cambio',
            'datsca': 'Data Scadenza',
            'pagato': 'Pagato',
            'codban': 'Codice Banca',
            'tippag': 'Tipo Pagamento',
        }
        widgets = {
            'numpro': forms.TextInput(attrs={'class':'numpro form-control pk l7', 'autocomplete': 'off', 'id': False}),
            'codfor': forms.TextInput(attrs={'class':'codfor form-control l5', 'autocomplete': 'off', 'id': False}),
            'tipdoc': forms.Select(attrs={'class':'tipdoc form-control l9', 'autocomplete': 'off', 'id': False}, choices=TIPDOC),
            'datdoc': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datdoc form-control l9', 'autocomplete': 'off', 'id': False}),
            'protoc': forms.NumberInput(attrs={'class':'protoc form-control l5', 'autocomplete': 'off', 'id': False}),
            'numfat': forms.NumberInput(attrs={'class':'numfat form-control l5', 'autocomplete': 'off', 'id': False}),
            'descri': forms.TextInput(attrs={'class':'descri form-control l35', 'autocomplete': 'off', 'id': False}),
            'impfat': forms.NumberInput(attrs={'class':'impfat form-control l13', 'autocomplete': 'off', 'id': False}),
            'imppag': forms.NumberInput(attrs={'class':'imppag form-control l13', 'autocomplete': 'off', 'id': False}),
            'codval': forms.TextInput(attrs={'class':'codval form-control l3', 'autocomplete': 'off', 'id': False}),
            'codpag': forms.TextInput(attrs={'class':'codpag form-control l4', 'autocomplete': 'off', 'id': False}),
            'modpag': forms.Select(attrs={'class':'modpag form-control l27', 'autocomplete': 'off', 'id': False}, choices=MODPAG),
            'cambio': forms.NumberInput(attrs={'class':'cambio form-control l11', 'autocomplete': 'off', 'id': False}),
            'datsca': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datsca form-control l9', 'autocomplete': 'off', 'id': False}),
            'pagato': forms.Select(attrs={'class':'pagato form-control l7', 'autocomplete': 'off', 'id': False}, choices=PAGATO),
            'codban': forms.TextInput(attrs={'class':'codban form-control l3', 'autocomplete': 'off', 'id': False}),
            'tippag': forms.Select(attrs={'class':'tippag form-control l11', 'autocomplete': 'off', 'id': False}, choices=TIPPAG),
        }
    def clean_numpro(self, *args, **kwargs):
        numpro = self.cleaned_data.get('numpro')
        if Scafor.objects.last() is not None:
            if numpro > int(Scafor.objects.last().pk) + 1:
                raise forms.ValidationError(f"Numero progressivo sbagliato, usare {int(Scafor.objects.last().pk) + 1}")
            else:
                return numpro
        else:
            if numpro != 1:
                raise forms.ValidationError(f"Numero progressivo sbagliato, usare {1}")
            else:
                return numpro
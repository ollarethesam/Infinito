from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.modpag import Modpag

class ModpagForm(ModelForm):
    class Meta:
        TIPPAG = [
        ("BB", "Bonifico Bancario"),
        ("D", "Diretto"),
        ("PP", "Pareggio Partita"),
        ("RB", "Ricevuta Bancaria"),
        ("T", "Tratta"),
        ]
        TIPSCA = [
        ("DD", "Data Diversa"),
        ("DF", "Data Fattura"),
        ("FM", "Fine Mese"),
        ]
        ESCMES = [
        ("A", "Agosto"),
        ("AD", "Agosto + Dicembre"),
        ("D", "Dicembre"),
        ("NE", "No Esclusione"),
        ]
        MODPAG = [
        ("01", "MP01-Contanti"),
        ("02", "MP02-Assengno"),
        ("03", "MP03-Assengno Circolare"),
        ("04", "MP04-Contanti Presso Tesoreria"),
        ("05", "MP05-Bonifico"),
        ("06", "MP06-Valigia Cambiario"),
        ("0N", "MP07-Bollettino Bancario"),
        ("08", "MP08-Carta Di Pagamento"),
        ("09", "MP09-RID"),
        ("10", "MP10-RID Utente"),
        ("11", "MP11-RID Veloce"),
        ("12", "MP12-RIBA"),
        ("13", "MP13-MAV"),
        ("14", "MP14-Quietanza Erario"),
        ("15", "MP15-Giroconto su COnti di Contabilità Speciale"),
        ("16", "MP16-Domiciliazione Bancaria"),
        ("17", "MP17-Domiciliazione Postale"),
        ("18", "MP18-Bollettino di C/C Postale"),
        ("19", "MP19-SEPA Direct Debit"),
        ("20", "MP20-SEPA Direct Debit Core"),
        ("21", "MP21-SEPA Direct Debit B2B"),
        ("22", "MP22-Trattenuta su Somme Già Riscosse"),
        ]
        model = Modpag
        fields = ["codpag", "despag", "tippag", "numrat", "giosca", "period", "tipsca", "escmes", "scocas", "gifisc", "modpag"]
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
            'tipsca': forms.Select(attrs={'class':'tipsca form-control', 'autocomplete': 'off', 'id': False}, choices=TIPSCA),
            'escmes': forms.Select(attrs={'class':'escmes form-control', 'autocomplete': 'off', 'id': False}, choices=ESCMES),
            'scocas': forms.NumberInput(attrs={'class':'scocas form-control', 'autocomplete': 'off', 'id': False}),
            'gifisc': forms.NumberInput(attrs={'class':'gifisc form-control', 'autocomplete': 'off', 'id': False}),
            'modpag': forms.Select(attrs={'class':'modpag form-control', 'autocomplete': 'off', 'id': False}, choices=MODPAG),
        }
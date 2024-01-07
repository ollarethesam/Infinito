from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.client import Client

class ClientForm(ModelForm):
    despag = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'despag form-control greybg', 'readonly': True, 'id': False}))
    deszon = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'deszon form-control greybg', 'readonly': True, 'id': False}))
    desiva = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'desiva form-control greybg', 'readonly': True, 'id': False}))
    datric = forms.CharField(required = False,label='', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datric form-control greybg', 'autocomplete': 'off', 'readonly': True, 'id': False}))
    desval = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'desval form-control greybg', 'readonly': True, 'id': False}))
    descat = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'descat form-control greybg', 'readonly': True, 'id': False}))
    desnaz = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'desnaz form-control greybg', 'readonly': True, 'id': False}))
    desban = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'desban form-control greybg', 'readonly': True, 'id': False}))
    desest = forms.CharField(required = False,label='', widget=forms.TextInput(attrs={'class':'desest form-control greybg', 'readonly': True, 'id': False}))
    proimp = forms.CharField(required = False,label='Prog. Imponibile', widget=forms.TextInput(attrs={'class':'proimp form-control alright greybg', 'readonly': True, 'id': False}))
    proiva = forms.CharField(required = False,label='Prog. Iva', widget=forms.TextInput(attrs={'class':'proiva form-control alright greybg', 'readonly': True, 'id': False}))
    pronim = forms.CharField(required = False,label='Prog. Non Imponibile', widget=forms.TextInput(attrs={'class':'pronim form-control alright greybg', 'readonly': True, 'id': False}))
    proese = forms.CharField(required = False,label='Prog. Esente', widget=forms.TextInput(attrs={'class':'proese form-control alright greybg', 'readonly': True, 'id': False}))
    numfat = forms.CharField(required = False,label='Num. Fatture', widget=forms.TextInput(attrs={'class':'numfat form-control alright greybg', 'readonly': True, 'id': False}))
    nunocr = forms.CharField(required = False,label='Num. Note Credito', widget=forms.TextInput(attrs={'class':'nunocr form-control alright greybg', 'readonly': True, 'id': False}))
    class Meta:
        TIPFOR = [
        ("1", "Importo non Frazionato"),
        ("2", "Importo Frazionato"),
        ("3", "Corrispettivi Periodici"),
        ]

        SPLPAY = [
            ('1', 'Si'),
            ('0', 'No')
        ]
        model = Client
        fields = ['codcli', 'ragsoc', 'datagg', 'indiri', 'locali', 'provin', 'cap', 'rssped', 'dasped', 'insped', 'losped', 'prsped', 'capspe', 'telefo', 'cellul', 'telef1', 'fax', 'pec', 'email', 'sito', 'codfis', 'pariva', 'banapp', 'fido', 'codpag', 'codzon', 'sconto', 'codiva', 'codese', 'codcab', 'codabi', 'codval', 'codnaz', 'paese', 'cineur', 'cin', 'conto', 'codcat', 'chiusf', 'chiust', 'nome', 'spese', 'storic', 'codban', 'staest', 'tipfor', 'alias', 'spesom', 'fatema', 'impass', 'annass', 'coduni', 'splpay', 'despag', 'deszon', 'desiva', 'datric', 'desval', 'descat', 'desnaz', 'desban']

        labels = {
            'codcli' : 'Codice Cliente',
            'ragsoc' : 'Ragione Sociale',
            'datagg' : 'Dati Aggiuntivi',
            'indiri' : 'Indirizzo',
            'locali' : 'Località',
            'provin' : 'Provincia',
            'cap'    : 'CAP',
            'rssped' : 'Ragione Sociale',
            'dasped' : 'Dati Aggiuntivi',
            'insped' : 'Indirizzo',
            'losped' : 'Località',
            'prsped' : 'Provincia',
            'capspe' : 'CAP',
            'telefo' : 'Telefono 1',
            'cellul' : 'Cellulare',
            'telef1' : 'Telefono 2',
            'fax'    : 'Fax',
            'pec'    : 'PEC',
            'email'  : 'Email',
            'sito'   : 'Sito',
            'codfis' : 'Codice Fiscale',
            'pariva' : 'Partita IVA',
            'banapp' : 'Banca d\'Appoggio',
            'fido'   : 'Fido',
            'codpag' : 'Pagamento',
            'codzon' : 'Zona',
            'sconto' : 'Sconto',
            'codiva' : 'Iva',
            'codese' : 'Esenzione',
            'codcab' : 'CAB',
            'codabi' : 'ABI',
            'codval' : 'Valuta',
            'codnaz' : 'Nazione',
            'paese'  : 'Paese',
            'cineur' : 'CinEur',
            'cin'    : 'Cin',
            'conto'  : 'N° Conto',
            'codcat' : ' Categoria',
            'chiusf' : 'Chiuso dal',
            'chiust' : 'Al',
            'nome'   : 'Nome',
            'spese'  : 'Spese',
            'storic' : 'Storico',
            'codban' : 'Banca',
            'staest' : 'Stato estero',
            'cognom' : 'Cognome',
            'comnas' : 'Comune di Nascita',
            'pronas' : 'Provinacia di Nascita',
            'datnas' : 'Data di Nascita',
            'tipfor' : 'Tipo Fornitura',
            'alias'  : 'Alias',
            'spesom' : 'Esclusione da Spesometro',
            'fatema' : 'Invio Fatture con Email',
            'impass' : 'Importo Assicurato',
            'annass' : 'Anno Assicurazione',
            'coduni' : 'Codice Univoco',
            'splpay' : 'Split Payment'
        }
        widgets = {
            'codcli' : forms.TextInput(attrs={'class':'codcli form-control pk l5', 'autocomplete': 'off', 'id': False}),
            'ragsoc' : forms.TextInput(attrs={'class':'ragsoc form-control l30', 'autocomplete': 'off', 'id': False}),
            'datagg' : forms.TextInput(attrs={'class':'datagg form-control', 'autocomplete': 'off', 'id': False}),
            'indiri' : forms.TextInput(attrs={'class':'indiri form-control', 'autocomplete': 'off', 'id': False}),
            'locali' : forms.TextInput(attrs={'class':'locali form-control', 'autocomplete': 'off', 'id': False}),
            'provin' : forms.TextInput(attrs={'class':'provin form-control l2', 'autocomplete': 'off', 'id': False}),
            'cap'    : forms.TextInput(attrs={'class':'cap form-control l5', 'autocomplete': 'off', 'id': False}),
            'rssped' : forms.TextInput(attrs={'class':'rssped form-control l30', 'autocomplete': 'off', 'id': False}),
            'dasped' : forms.TextInput(attrs={'class':'dasped form-control', 'autocomplete': 'off', 'id': False}),
            'insped' : forms.TextInput(attrs={'class':'insped form-control', 'autocomplete': 'off', 'id': False}),
            'losped' : forms.TextInput(attrs={'class':'losped form-control', 'autocomplete': 'off', 'id': False}),
            'prsped' : forms.TextInput(attrs={'class':'prsped form-control l2', 'autocomplete': 'off', 'id': False}),
            'capspe' : forms.TextInput(attrs={'class':'capspe form-control l5', 'autocomplete': 'off', 'id': False}),
            'telefo' : forms.TextInput(attrs={'class':'telefo form-control l13', 'autocomplete': 'off', 'id': False}),
            'cellul' : forms.TextInput(attrs={'class':'cellul form-control l13', 'autocomplete': 'off', 'id': False}),
            'telef1' : forms.TextInput(attrs={'class':'telef1 form-control l13', 'autocomplete': 'off', 'id': False}),
            'fax'    : forms.TextInput(attrs={'class':'fax form-control l15', 'autocomplete': 'off', 'id': False}),
            'pec'    : forms.TextInput(attrs={'class':'pec form-control', 'autocomplete': 'off', 'id': False}),
            'email'  : forms.TextInput(attrs={'class':'email form-control', 'autocomplete': 'off', 'id': False}),
            'sito'   : forms.TextInput(attrs={'class':'sito form-control', 'autocomplete': 'off', 'id': False}),
            'codfis' : forms.TextInput(attrs={'class':'codfis form-control l16', 'autocomplete': 'off', 'id': False}),
            'pariva' : forms.TextInput(attrs={'class':'pariva form-control l11', 'autocomplete': 'off', 'id': False}),
            'banapp' : forms.TextInput(attrs={'class':'banapp form-control', 'autocomplete': 'off', 'id': False}),
            'fido'   : forms.NumberInput(attrs={'class':'fido form-control l5 ', 'autocomplete': 'off','step':'0.01', 'id': False}),
            'codpag' : forms.TextInput(attrs={'class':'codpag form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'codzon' : forms.TextInput(attrs={'class':'codzon form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'sconto' : forms.NumberInput(attrs={'class':'sconto form-control', 'autocomplete': 'off','step':'0.01', 'id': False}),
            'codiva' : forms.TextInput(attrs={'class':'codiva form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'codese' : forms.TextInput(attrs={'class':'codese form-control fk l4', 'autocomplete': 'off', 'id': False}),
            'codcab' : forms.TextInput(attrs={'class':'codcab form-control l4', 'autocomplete': 'off', 'id': False}),
            'codabi' : forms.TextInput(attrs={'class':'codabi form-control l5', 'autocomplete': 'off', 'id': False}),
            'codval' : forms.TextInput(attrs={'class':'codval form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'codnaz' : forms.TextInput(attrs={'class':'codnaz form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'paese'  : forms.TextInput(attrs={'class':'paese form-control l2', 'autocomplete': 'off', 'id': False}),
            'cineur' : forms.TextInput(attrs={'class':'cineur form-control l2', 'autocomplete': 'off', 'id': False}),
            'cin'    : forms.TextInput(attrs={'class':'cin form-control l1', 'autocomplete': 'off', 'id': False}),
            'conto'  : forms.TextInput(attrs={'class':'conto form-control l12', 'autocomplete': 'off', 'id': False}),
            'codcat' : forms.TextInput(attrs={'class':'codcat form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'chiusf' : forms.DateInput(format='%d-%m', attrs={'type':'date', 'class':'chiusf  form-control', 'autocomplete': 'off', 'id': False}),
            'chiust' : forms.DateInput(format='%d-%m', attrs={'type':'date', 'class':'chiust  form-control', 'autocomplete': 'off', 'id': False}),
            'nome'   : forms.TextInput(attrs={'class':'nome form-control', 'autocomplete': 'off', 'id': False}),
            'spese'  : forms.CheckboxInput(attrs={'class':'spese form-control checkbox', 'autocomplete': 'off', 'required': False, 'id': False}),
            'storic' : forms.CheckboxInput(attrs={'class':'storic form-control checkbox', 'autocomplete': 'off', 'required': False, 'id': False}),
            'codban' : forms.TextInput(attrs={'class':'codban form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'staest' : forms.TextInput(attrs={'class':'staest form-control l2', 'autocomplete': 'off', 'id': False}),
            'cognom' : forms.TextInput(attrs={'class':'cognom form-control', 'autocomplete': 'off', 'id': False}),
            'comnas' : forms.TextInput(attrs={'class':'comnas form-control', 'autocomplete': 'off', 'id': False}),
            'pronas' : forms.TextInput(attrs={'class':'pronas form-control', 'autocomplete': 'off', 'id': False}),
            'datnas' : forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datnas  form-control', 'autocomplete': 'off', 'id': False}),
            'tipfor' : forms.Select(attrs={'class':'tipfor form-control', 'autocomplete': 'off', 'id': False}, choices=TIPFOR),
            'alias'  : forms.TextInput(attrs={'class':'alias form-control', 'autocomplete': 'off', 'id': False}),
            'tipcli' : forms.TextInput(attrs={'class':'tipcli form-control short', 'autocomplete': 'off', 'id': False}),
            'spesom' : forms.CheckboxInput(attrs={'class':'spesom form-control checkbox', 'autocomplete': 'off', 'required': False, 'id': False}),
            'fatema' : forms.CheckboxInput(attrs={'class':'fatema form-control checkbox', 'autocomplete': 'off', 'required': False, 'id': False}),
            'impass' : forms.NumberInput(attrs={'class':'impass form-control short', 'autocomplete': 'off','step':'0.01', 'id': False}),
            'annass' : forms.TextInput(attrs={'class':'annass form-control short', 'autocomplete': 'off', 'id': False}),
            'coduni' : forms.TextInput(attrs={'class':'coduni form-control short', 'autocomplete': 'off', 'id': False}),
            'splpay' : forms.Select(attrs={'class':'splpay form-control short', 'autocomplete': 'off', 'id': False}, choices=SPLPAY),
        }

        
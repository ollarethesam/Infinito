from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm
from DataManager.models.fornit import Fornit

class FornitForm(ModelForm):
    despag = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'despag form-control', 'readonly': True, 'id': False}))
    deszon = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'deszon form-control', 'readonly': True, 'id': False}))
    desiva = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'desiva form-control', 'readonly': True, 'id': False}))
    descat = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'descat form-control', 'readonly': True, 'id': False}))
    desnaz = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'desnaz form-control', 'readonly': True, 'id': False}))
    desban = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'desban form-control', 'readonly': True, 'id': False}))
    desest = forms.CharField(required = False, label='', widget=forms.TextInput(attrs={'class':'desest form-control', 'readonly': True, 'id': False}))
    proimp = forms.CharField(required = False, label='Prog. Imponibile', widget=forms.TextInput(attrs={'class':'proimp form-control alright greybg', 'readonly': True, 'id': False}))
    proiva = forms.CharField(required = False, label='Prog. Iva', widget=forms.TextInput(attrs={'class':'proiva form-control alright greybg', 'readonly': True, 'id': False}))
    pronim = forms.CharField(required = False, label='Prog. Non Imponibile', widget=forms.TextInput(attrs={'class':'pronim form-control alright greybg', 'readonly': True, 'id': False}))
    proese = forms.CharField(required = False, label='Prog. Esente', widget=forms.TextInput(attrs={'class':'proese form-control alright greybg', 'readonly': True, 'id': False}))
    numfat = forms.CharField(required = False, label='Num. Fatture', widget=forms.TextInput(attrs={'class':'numfat form-control alright greybg', 'readonly': True, 'id': False}))
    nunocr = forms.CharField(required = False, label='Num. Note Credito', widget=forms.TextInput(attrs={'class':'nunocr form-control alright greybg', 'readonly': True, 'id': False}))
    class Meta:
        TIPFOR = [
        ("1", "Importo non Frazionato"),
        ("2", "Importo Frazionato"),
        ("3", "Corrispettivi Periodici"),
        ]
        REGFIS = [
        ("01", "RF01-Ordinario"),
        ("02", "RF02-Contribuenti Minimi"),
        ("04", "RF03-Agricoltura e Attività Connesse Pesca"),
        ("05", "RF05-Vendita Sale e Tabacchi"),
        ("06", "RF06-Commercio FIammiferi"),
        ("0N", "RF07-Editoria"),
        ("08", "RF08-Gestione Servizi Telefonia Pubblica"),
        ("09", "RF09-Rivendita Documenti di Trasporto e di Sosta"),
        ("10", "RF10-Intrattenimento e Giochi"),
        ("11", "RF11-Agenzie di Viaggio e Turismo"),
        ("12", "RF12-Agriturismo"),
        ("13", "RF13-Vendite a Domicilio"),
        ("14", "RF14-Rivendita Beni Usati, Oggetti d'Arte, Antiquariato o da Collezione"),
        ("15", "RF15-Agenzie di Vendita all'Asta di oggetti d'arte, Anquariato o da Collezione"),
        ("16", "RF16-IVA per Cassa P.A."),
        ("17", "RF17-IVA per Cassa"),
        ("18", "RF18-Altro"),
        ("19", "RF19-Regime Forfettario"),
        ]
        model = Fornit
        fields = ['codfor', 'ragsoc', 'datagg', 'indiri', 'locali', 'provin', 'cap', 'codfis', 'pariva', 'telef1', 'telef2', 'cellul', 'fax', 'email', 'sito', 'codpag', 'pae', 'cineur', 'cin', 'conto', 'codabi', 'codcab', 'banapp', 'codnaz', 'codiva', 'codcat', 'codzon', 'codban', 'storic', 'staest', 'tipfor', 'spesom', 'schcar', 'alias', 'regfis', 'despag', 'deszon', 'desiva', 'descat', 'desnaz', 'desban']
        labels = {
            'codfor': 'Codice Fornitore',
            'ragsoc': 'Ragione Sociale',
            'datagg': 'Dati Aggiuntivi',
            'indiri': 'Indirizzo',
            'locali': 'Località',
            'provin': 'Provincia',
            'cap'   : 'CAP',
            'codfis': 'Codice Fiscale',
            'pariva': 'Partita IVA',
            'telef1': 'Telefono 1',
            'telef2': 'Telefono 2',
            'cellul': 'Cellulare',
            'fax'   : 'Fax',
            'email' : 'Email',
            'sito'  : 'Sito',
            'codpag': 'Cod. Pagamento',
            'pae'   : 'Paese',
            'cineur': 'CinEur',
            'cin'   : 'Cin',
            'conto' : 'N. Conto',
            'codabi': 'ABI',
            'codcab': 'CAB',
            'banapp': 'Banca d\'Appoggio',
            'codnaz': 'Cod. Nazione',
            'codiva': 'Cod. IVA',
            'codcat': 'Cod. Categoria',
            'codzon': 'Cod. Zona',
            'codban': 'Cod. Banca',
            'storic': 'Storico',
            'staest': 'Cod. Stato Estero',
            'cognom': 'Cognome',
            'nome'  : 'Nome',
            'datnas': 'Data di Nascita',
            'tipfor': 'Tipo Fornitura',
            'spesom': 'Esclusione Da Spesometro',
            'schcar': 'Scheda Carburante',
            'alias' : 'Alias',
            'regfis': 'Regime Fiscale',
        }
        widgets = {
            'codfor': forms.TextInput(attrs={'class':'codfor form-control pk l5', 'autocomplete': 'off', 'id': False}),
            'ragsoc': forms.TextInput(attrs={'class':'ragsoc form-control l30', 'autocomplete': 'off', 'id': False}),
            'datagg': forms.TextInput(attrs={'class':'datagg form-control', 'autocomplete': 'off', 'id': False}),
            'indiri': forms.TextInput(attrs={'class':'indiri form-control', 'autocomplete': 'off', 'id': False}),
            'locali': forms.TextInput(attrs={'class':'locali form-control', 'autocomplete': 'off', 'id': False}),
            'provin': forms.TextInput(attrs={'class':'provin form-control l2', 'autocomplete': 'off', 'id': False}),
            'cap'   : forms.TextInput(attrs={'class':'cap form-control l5', 'autocomplete': 'off', 'id': False}),
            'codfis': forms.TextInput(attrs={'class':'codfis form-control l16', 'autocomplete': 'off', 'id': False}),
            'pariva': forms.TextInput(attrs={'class':'pariva form-control l11', 'autocomplete': 'off', 'id': False}),
            'telef1': forms.TextInput(attrs={'class':'telef1 form-control l13', 'autocomplete': 'off', 'id': False}),
            'telef2': forms.TextInput(attrs={'class':'telef2 form-control l13', 'autocomplete': 'off', 'id': False}),
            'cellul': forms.TextInput(attrs={'class':'cellul form-control l13', 'autocomplete': 'off', 'id': False}),
            'fax'   : forms.TextInput(attrs={'class':'fax form-control l15', 'autocomplete': 'off', 'id': False}),
            'email' : forms.TextInput(attrs={'class':'email form-control', 'autocomplete': 'off', 'id': False}),
            'sito'  : forms.TextInput(attrs={'class':'sito form-control', 'autocomplete': 'off', 'id': False}),
            'codpag': forms.TextInput(attrs={'class':'codpag form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'pae'   : forms.TextInput(attrs={'class':'pae form-control l2', 'autocomplete': 'off', 'id': False}), 
            'cineur': forms.TextInput(attrs={'class':'cineur form-control l2', 'autocomplete': 'off', 'id': False}),
            'cin'   : forms.TextInput(attrs={'class':'cin form-control l1', 'autocomplete': 'off', 'id': False}),
            'conto' : forms.TextInput(attrs={'class':'conto form-control l12', 'autocomplete': 'off', 'id': False}),
            'codabi': forms.TextInput(attrs={'class':'codabi form-control l5', 'autocomplete': 'off', 'id': False}),
            'codcab': forms.TextInput(attrs={'class':'codcab form-control l4', 'autocomplete': 'off', 'id': False}),
            'banapp': forms.TextInput(attrs={'class':'banapp form-control', 'autocomplete': 'off', 'id': False}),
            'codnaz': forms.TextInput(attrs={'class':'codnaz form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'codiva': forms.TextInput(attrs={'class':'codiva form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'codcat': forms.TextInput(attrs={'class':'codcat form-control fk l2', 'autocomplete': 'off', 'id': False}),
            'codzon': forms.TextInput(attrs={'class':'codzon form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'codban': forms.TextInput(attrs={'class':'codban form-control fk l3', 'autocomplete': 'off', 'id': False}),
            'storic': forms.CheckboxInput(attrs={'class':'storic form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'staest': forms.TextInput(attrs={'class':'staest form-control l2', 'autocomplete': 'off', 'id': False}),
            'cognom': forms.TextInput(attrs={'class':'cognom form-control', 'autocomplete': 'off', 'id': False}),
            'nome'  : forms.TextInput(attrs={'class':'nome form-control', 'autocomplete': 'off', 'id': False}),
            'datnas': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datnas form-control', 'autocomplete': 'off', 'id': False}),
            'tipfor': forms.Select(attrs={'class':'tipfor form-control', 'autocomplete': 'off', 'id': False}, choices=TIPFOR),
            'schcar': forms.CheckboxInput(attrs={'class':'schcar form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'copfat': forms.CheckboxInput(attrs={'class':'copfat form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'noncon': forms.CheckboxInput(attrs={'class':'noncon form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'alias' : forms.TextInput(attrs={'class':'alias form-control', 'autocomplete': 'off', 'id': False}),
            'regfis': forms.Select(attrs={'class':'regfis form-control', 'autocomplete': 'off', 'id': False}, choices=REGFIS),
        }
    def clean_codfor(self, *args, **kwargs):
        codfor = self.cleaned_data.get('codfor')
        if len(codfor) != 5:
            raise forms.ValidationError("Il codice fornitore deve essre lungo 5 caratteri")
        else:
            return codfor
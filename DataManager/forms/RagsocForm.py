from DataManager.models.ragsoc import Ragsoc
from email.policy import default
from signal import raise_signal
from django import forms
from django.forms import ModelForm

class RagsocForm(ModelForm):
    class Meta:
        SESSO = [
            ('M', 'Maschio'),
            ('F', 'Femmina')
        ]
        TIPCON = [
            ('1', 'Ordinaria'),
            ('2', 'Semplificata')
        ]
        TIPIVA = [
            ('1', 'Standard'),
            ('2', 'Regime IVA TER'),
            ('3', 'Mista IVA 50%'),
            ('4', 'Arti e Professioni IVA 84%'),
            ('5', 'Prestazioni di Servizi IVA 73%'),
            ('6', 'Altri IVA 60%'),
            ('7', 'Prorata'),
            ('8', 'Sospensione d\'Imposta')
        ]
        TIPSOG=[
            ('01', 'Soggetti che inviano le proprie comunicazioni'),
            ('10', 'CAF Dipendenti e pensionati, imprese, società ART. 3, altri intermediari')
        ]
        COMPRE = [
            ('1', 'Contribuente'),
            ('2', 'Intermediario')
        ]
        REGFIS = [
        ("01", "RF01-Ordinario"),
        ("02", "RF02-Contribuenti Minimi"),
        ("04", "RF03-Agricoltura e Attività Connesse Pesca"),
        ("05", "RF05-Vendita Sale e Tabacchi"),
        ("06", "RF06-Commercio Fiammiferi"),
        ("07", "RF07-Editoria"),
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

        SOCUNI = [
            ('SU', 'Socio Unico'),
            ('SM', 'Più Soci')
        ]
        STALIQ = [
            ('LS', 'In Liquidazione'),
            ('LN', 'Non in Liquidazione')
        ]
        model = Ragsoc
        fields = [
            "datini", "ragsoc", "indiri", "locali", "cap", "provin", "pariva", "codfis",
            "email", "sito", "corven", "art10", "ditind", "sesso", "datnas", "comnas",
            "pronas", "cognom", "nome", "tipsog", "tipcon", "tipiva", "banapp", "iban",
            "cofiin", "iscain", "compre", "cofiso", "codatt", "gescor", "regfis", "isrepr",
            "isrenu", "capsoc", "socuni", "staliq",

            "maclit", "macles", "masfor", "ivcove", "ivcoac", "ivcoco", "cassa", "cotrri",
            "spetra", "spebol", "speinc", "picfat", "portra", "poriba", "conven", "copapa",
            "ivacce", "ivvece", "ivacre", "ivvere", "coriac", "conena", "cocoin", "ivvesp",

            "coivtr", "coivbo", "coivin", "coivpi", "coivta", "coivri",

            "ritenu", "imponi", "enasar", "ritena", "impena"
        ]
        labels = {
            'datini':'Data Inizio',
            'ragsoc':'Ragione Sociale',
            'indiri':'Indirizzo',
            'locali':'Località',
            'cap'   :'Cap',
            'provin':'Provincia',
            'pariva':'Partita IVA',
            'codfis':'Codice Fiscale',
            'email' :'Email',
            'sito'  :'Sito',
            'corven':'Codice IVA Corrispettivi da Ventilare',
            'art10' :'Codice IVA Art. 10',
            'ditind':'Ditta Individuale',
            'sesso' :'Sesso',
            'datnas':'Data di Nascita',
            'comnas':'Comune o Stato Estero di Nascita',
            'pronas':'Provincia di Nascita',
            'cognom':'Cognome',
            'nome'  :'Nome',
            'tipsog':'Tipo Soggetto',
            'tipcon':'Tipo Contabilità',
            'tipiva':'Tipo IVA',
            'banapp':'Banca d\'appoggio',
            'iban'  :'Iban',
            'cofiin':'Codice Fiscale Intermediario',
            'iscain':'Numero Iscrizione CAF Intermediario',
            'compre':'Comunicazione Predisposta da',
            'cofiso':'Codice Fiscale Soggetto Obbligato',
            'codatt':'Codice Attività',
            'gescor':'Gestione Corrispettivi',
            'regfis':'Regime Fiscale',
            'isrepr':'Iscrizione REA Provincia',
            'isrenu':'Iscrizione REA Numero',
            'capsoc':'Capitale Sociale',
            'socuni':'Socio Unico',
            'staliq':'Stato Liquidazione',
            'maclit':'Mastro Clienti Italia',
            'macles':'Mastro Clienti Estero',
            'masfor':'Mastro Fornitori',
            'ivcove':'IVA Conto Vendite',
            'ivcoac':'IVA Conto Acquisti Detraibile',
            'ivcoco':'IVA Conto Corrispettivi',
            'cassa' :'Cassa',
            'cotrri':'Conto Transitorio Ricavi',
            'spetra':'Spese Trasporto',
            'spebol':'Spese Bollo',
            'speinc':'Spese Incasso',
            'picfat':'Piccola Fatturazione',
            'portra':'Portafoglio Tratte',
            'poriba':'Portafoglio Ricevute Bancarie',
            'conven':'Conto Vendita',
            'copapa':'Conto Pareggio Partita',
            'ivacce':'IVA Conto Acquisti CEE',
            'ivvece':'IVA Conto Vendite CEE',
            'ivacre':'IVA Conto Acquisti Reverse Charge',
            'ivvere':'IVA Conto Vendite Reverse Charge',
            'coriac':'Conto Ritenuta d\'Acconto',
            'conena':'Conto Enasarco',
            'cocoin':'Conto Costo Indetraibile',
            'ivvesp':'IVA Vendite Split Payment',
            'coivtr':'Codice IVA Trasporto',
            'coivbo':'Codice IVA Bollo',
            'coivin':'Codice IVA Incasso',
            'coivpi':'Codice IVA Piccola Fatturazione',
            'coivta':'Codice IVA Tratte',
            'coivri':'Codice IVA Ricevute Bancarie',
            'ritenu':'% Ritenuta',
            'imponi':'% Imponibile',
            'enasar':'% Enasarco',
            'ritena':'% Ritenuta Enasarco',
            'impena':'% Imponibile Enasarco'
        }
        widgets = {
            'datini': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datini form-control l9', 'autocomplete': 'off', 'id': False}),
            'ragsoc': forms.TextInput(attrs={'class':'ragsoc form-control l35', 'autocomplete': 'off', 'id': False}), 
            'indiri': forms.TextInput(attrs={'class':'indiri form-control l35', 'autocomplete': 'off', 'id': False}),
            'locali': forms.TextInput(attrs={'class':'locali form-control l35', 'autocomplete': 'off', 'id': False}),
            'cap'   : forms.TextInput(attrs={'class':'cap form-control l5', 'autocomplete': 'off', 'id': False}),
            'provin': forms.TextInput(attrs={'class':'provin form-control l2', 'autocomplete': 'off', 'id': False}),
            'pariva': forms.TextInput(attrs={'class':'pariva form-control l11', 'autocomplete': 'off', 'id': False}),
            'codfis': forms.TextInput(attrs={'class':'codfis form-control l16', 'autocomplete': 'off', 'id': False}),
            'email' : forms.TextInput(attrs={'class':'email form-control l35', 'autocomplete': 'off', 'id': False}),
            'sito'  : forms.TextInput(attrs={'class':'sito form-control l35', 'autocomplete': 'off', 'id': False}),
            'corven': forms.TextInput(attrs={'class':'corven form-control l2', 'autocomplete': 'off', 'id': False}),
            'art10' : forms.TextInput(attrs={'class':'art10 form-control l2', 'autocomplete': 'off', 'id': False}),
            'ditind': forms.CheckboxInput(attrs={'class':'ditind form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'sesso' : forms.Select(attrs={'class':'sesso form-control l7', 'autocomplete': 'off', 'id': False}, choices=SESSO),
            'datnas': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date', 'class':'datnas form-control l9', 'autocomplete': 'off', 'id': False}),
            'comnas': forms.TextInput(attrs={'class':'comnas form-control l35', 'autocomplete': 'off', 'id': False}),
            'pronas': forms.TextInput(attrs={'class':'pronas form-control l2', 'autocomplete': 'off', 'id': False}),
            'cognom': forms.TextInput(attrs={'class':'cognom form-control l35', 'autocomplete': 'off', 'id': False}),
            'nome'  : forms.TextInput(attrs={'class':'nome form-control l35', 'autocomplete': 'off', 'id': False}),
            'tipcon': forms.Select(attrs={'class':'tipcon form-control l9', 'autocomplete': 'off', 'id': False}, choices=TIPCON),
            'tipiva': forms.Select(attrs={'class':'tipiva form-control l16', 'autocomplete': 'off', 'id': False}, choices=TIPIVA),
            'tipsog': forms.Select(attrs={'class':'tipsog form-control l35', 'autocomplete': 'off', 'id': False}, choices=TIPSOG),
            'banapp': forms.TextInput(attrs={'class':'banapp form-control l35', 'autocomplete': 'off', 'id': False}),
            'iban'  : forms.TextInput(attrs={'class':'iban form-control l27', 'autocomplete': 'off', 'id': False}),
            'cofiin': forms.TextInput(attrs={'class':'cofiin form-control l16', 'autocomplete': 'off', 'id': False}),
            'iscain': forms.TextInput(attrs={'class':'iscain form-control l5', 'autocomplete': 'off', 'id': False}),
            'compre': forms.Select(attrs={'class':'compre form-control l9', 'autocomplete': 'off', 'id': False}, choices=COMPRE),
            'cofiso': forms.TextInput(attrs={'class':'cofiso form-control l16', 'autocomplete': 'off', 'id': False}),
            'codatt': forms.TextInput(attrs={'class':'codatt form-control l6', 'autocomplete': 'off', 'id': False}),
            'gescor': forms.CheckboxInput(attrs={'class':'gescor form-control checkbox', 'autocomplete': 'off', 'id': False}),
            'regfis': forms.Select(attrs={'class':'regfis form-control l35', 'autocomplete': 'off', 'id': False}, choices=REGFIS),
            'isrepr': forms.TextInput(attrs={'class':'isrepr form-control l2', 'autocomplete': 'off', 'id': False}),
            'isrenu': forms.TextInput(attrs={'class':'isrenu form-control l6', 'autocomplete': 'off', 'id': False}),
            'capsoc': forms.TextInput(attrs={'class':'capsoc form-control l15', 'autocomplete': 'off', 'id': False}),
            'socuni': forms.Select(attrs={'class':'socuni form-control l9', 'autocomplete': 'off', 'id': False}, choices=SOCUNI),
            'staliq': forms.Select(attrs={'class':'staliq form-control l15', 'autocomplete': 'off', 'id': False}, choices=STALIQ),
            'maclit': forms.TextInput(attrs={'class':'maclit form-control l9', 'autocomplete': 'off', 'id': False}),
            'macles': forms.TextInput(attrs={'class':'macles form-control l9', 'autocomplete': 'off', 'id': False}),
            'masfor': forms.TextInput(attrs={'class':'masfor form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivcove': forms.TextInput(attrs={'class':'ivcove form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivcoac': forms.TextInput(attrs={'class':'ivcoac form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivcoco': forms.TextInput(attrs={'class':'ivcoco form-control l9', 'autocomplete': 'off', 'id': False}),
            'cassa' : forms.TextInput(attrs={'class':'cassa  form-control l9', 'autocomplete': 'off', 'id': False}),
            'cotrri': forms.TextInput(attrs={'class':'cotrri form-control l9', 'autocomplete': 'off', 'id': False}),
            'spetra': forms.TextInput(attrs={'class':'spetra form-control l9', 'autocomplete': 'off', 'id': False}),
            'spebol': forms.TextInput(attrs={'class':'spebol form-control l9', 'autocomplete': 'off', 'id': False}),
            'speinc': forms.TextInput(attrs={'class':'speinc form-control l9', 'autocomplete': 'off', 'id': False}),
            'picfat': forms.TextInput(attrs={'class':'picfat form-control l9', 'autocomplete': 'off', 'id': False}),
            'portra': forms.TextInput(attrs={'class':'portra form-control l9', 'autocomplete': 'off', 'id': False}),
            'poriba': forms.TextInput(attrs={'class':'poriba form-control l9', 'autocomplete': 'off', 'id': False}),
            'conven': forms.TextInput(attrs={'class':'conven form-control l9', 'autocomplete': 'off', 'id': False}),
            'copapa': forms.TextInput(attrs={'class':'copapa form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivacce': forms.TextInput(attrs={'class':'ivacce form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivvece': forms.TextInput(attrs={'class':'ivvece form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivacre': forms.TextInput(attrs={'class':'ivacre form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivvere': forms.TextInput(attrs={'class':'ivvere form-control l9', 'autocomplete': 'off', 'id': False}),
            'coriac': forms.TextInput(attrs={'class':'coriac form-control l9', 'autocomplete': 'off', 'id': False}),
            'conena': forms.TextInput(attrs={'class':'conena form-control l9', 'autocomplete': 'off', 'id': False}),
            'cocoin': forms.TextInput(attrs={'class':'cocoin form-control l9', 'autocomplete': 'off', 'id': False}),
            'ivvesp': forms.TextInput(attrs={'class':'ivvesp form-control l9', 'autocomplete': 'off', 'id': False}),
            'coivbo': forms.TextInput(attrs={'class':'coivbo form-control l2', 'autocomplete': 'off', 'id': False}),
            'coivin': forms.TextInput(attrs={'class':'coivin form-control l2', 'autocomplete': 'off', 'id': False}),
            'coivtr': forms.TextInput(attrs={'class':'coivtr form-control l2', 'autocomplete': 'off', 'id': False}),
            'coivpi': forms.TextInput(attrs={'class':'coivpi form-control l2', 'autocomplete': 'off', 'id': False}),
            'coivta': forms.TextInput(attrs={'class':'coivta form-control l2', 'autocomplete': 'off', 'id': False}),
            'coivri': forms.TextInput(attrs={'class':'coivri form-control l2', 'autocomplete': 'off', 'id': False}),
            'ritenu': forms.NumberInput(attrs={'class':'ritenu form-control l5', 'autocomplete': 'off', 'id': False}),
            'imponi': forms.NumberInput(attrs={'class':'imponi form-control l5', 'autocomplete': 'off', 'id': False}),
            'enasar': forms.NumberInput(attrs={'class':'enasar form-control l5', 'autocomplete': 'off', 'id': False}),
            'ritena': forms.NumberInput(attrs={'class':'ritena form-control l5', 'autocomplete': 'off', 'id': False}),
            'impena': forms.NumberInput(attrs={'class':'impena form-control l5', 'autocomplete': 'off', 'id': False}),
        }
from importlib import *
from django.urls import path, include
from .views.__init__ import __all__
for i in __all__:
    exec(f'from .views.{i} import {i}')

urlpatterns = [
    path('', menu, name='menu'),
    path('Gestione-Tabella-Banche', banche, name='banche'),
    path('Gestione-Tabella-Categorie', catego, name='catego'),
    path('Clienti', client, name='client'),
    path('Fornitori', fornit, name="fornit"),
    path('Gestione-Destinatari-Clienti', destcl, name='destcl'),
    path('Gestione-Destinatari-Fornitori', destfo, name="destfo"),
    path('Esenzione-IVA', eseiva, name='eseiva'),
    path('Modalita-di-Pagamento', modpag, name='modpag'),
    path('Gestione-Tabella-Nazioni', nazion, name='nazion'),
    path('Valute', valute, name='valute'),
    path('Zone', zone, name='zone'),
    path('Tabella-IVA-Vendite', ivaven, name='ivaven'),
    path('Agenti', agenti, name='agenti'),
    path('Agenti', agenti, name='agenti'),
    path('Gestione-Articoli', artico, name="artico"),
    path('Aspetto-Esteriore', aspest, name="aspest"),
    path('Categorie-Contabili', catcon, name="catcon"),
    path('Piano-dei-Conti', piacon, name="piacon"),
    path('Causali-Trasporto', cautra, name="cautra"),
    path('Gestione-Centri-di-Lavoro', cenlav, name="cenlav"),
    path('Des-Gruppi-Art', degrar, name="degrar"),
    path('Gestione-Dipendenti', dipend, name="dipend"),
    path('Tabella-IVA-Corrispettivi', ivacor, name="ivacor"),
    path('Tabella-IVA-Acquisti', ivaacq, name="ivaacq"),
    path('Porto', porto, name="porto"),
    path('Raggruppamenti-Fiscali', raggfi, name="raggfi"),
    path('Spedizioni', spediz, name="spediz"),
    path('Tipi-Allegati', tipall, name="tipall"),
    path('Gestione-Prezzi-per-Cliente', liscli, name="liscli"),
    path('Gestione-Scadenziario-Clienti', scacli, name="scacli"),
    path('Gestione-Scadenziario-Fornitori', scafor, name="scafor"),
    path('Ragione-Sociale-Utente', ragsoc, name="ragsoc"),
    path('Gestione-Movimenti-Magazzino', movmag, name="movmag"),
    path('Gestione-Causali-Magazzino', caumag, name="caumag"),
]
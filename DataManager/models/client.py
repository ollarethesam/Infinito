from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .banche import Banche
from .modpag import Modpag
from .zone import Zone
from .eseiva import Eseiva
from .valute import Valute
from .nazion import Nazion
from .catego import Catego
from .ivaven import Ivaven

class Client(models.Model):
    codcli = models.CharField(primary_key=True, max_length=5)
    ragsoc = models.CharField(max_length=40)
    datagg = models.CharField(max_length=40)
    indiri = models.CharField(max_length=40)
    locali = models.CharField(max_length=30)
    provin = models.CharField(max_length=2)
    cap    = models.CharField(max_length=5)
    rssped = models.CharField(max_length=40)
    dasped = models.CharField(max_length=40)
    insped = models.CharField(max_length=40)
    losped = models.CharField(max_length=30)
    prsped = models.CharField(max_length=2)
    capspe = models.CharField(max_length=5)
    telefo = models.CharField(max_length=15)
    cellul = models.CharField(max_length=15)
    telef1 = models.CharField(max_length=15)
    fax    = models.CharField(max_length=15)
    pec    = models.CharField(max_length=80)
    email  = models.CharField(max_length=40)
    sito   = models.CharField(max_length=40)
    codfis = models.CharField(max_length=16)
    pariva = models.CharField(max_length=20)
    banapp = models.CharField(max_length=40)
    fido   = models.IntegerField()
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE)
    codzon = models.ForeignKey(Zone, to_field='codzon', on_delete=models.CASCADE)
    sconto = models.IntegerField()
    codiva = models.ForeignKey(Ivaven, to_field='codiva', on_delete=models.CASCADE)
    codese = models.ForeignKey(Eseiva, to_field='codese', on_delete=models.CASCADE)
    codcab = models.CharField(max_length=5)
    codabi = models.CharField(max_length=5)
    codval = models.ForeignKey(Valute, to_field='codval', on_delete=models.CASCADE)
    codnaz = models.ForeignKey(Nazion, to_field='codnaz', on_delete=models.CASCADE)
    paese  = models.CharField(max_length=2)
    cineur = models.CharField(max_length=2)
    cin    = models.CharField(max_length=1)
    conto  = models.CharField(max_length=12)
    codcat = models.ForeignKey(Catego, to_field='codcat', on_delete=models.CASCADE)
    chiusf = models.DateField()
    chiust = models.DateField()
    nome   = models.CharField(max_length=30)
    spese  = models.BooleanField(default=False)
    storic = models.BooleanField(default=False)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE)
    staest = models.CharField(max_length=3)
    tipfor = models.IntegerField()
    alias  = models.CharField(max_length=40)
    spesom = models.BooleanField(default=False)
    fatema = models.BooleanField(default=False)
    impass = models.IntegerField()
    annass = models.CharField(max_length=4)
    coduni = models.CharField(max_length=7)
    splpay = models.CharField(max_length=1)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        db_table = 'client'
        managed = True

    def __str__(self):
        return f"{self.codcli} - {self.ragsoc}"
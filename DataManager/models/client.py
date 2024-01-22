from django.db import models
from Login.models import CustomUser
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
    datagg = models.CharField(max_length=40, null=True, blank=True)
    indiri = models.CharField(max_length=40, null=True, blank=True)
    locali = models.CharField(max_length=30, null=True, blank=True)
    provin = models.CharField(max_length=2, null=True, blank=True)
    cap    = models.CharField(max_length=5, null=True, blank=True)
    rssped = models.CharField(max_length=40, null=True, blank=True)
    dasped = models.CharField(max_length=40, null=True, blank=True)
    insped = models.CharField(max_length=40, null=True, blank=True)
    losped = models.CharField(max_length=30, null=True, blank=True)
    prsped = models.CharField(max_length=2, null=True, blank=True)
    capspe = models.CharField(max_length=5, null=True, blank=True)
    telefo = models.CharField(max_length=15, null=True, blank=True)
    cellul = models.CharField(max_length=15, null=True, blank=True)
    telef1 = models.CharField(max_length=15, null=True, blank=True)
    fax    = models.CharField(max_length=15, null=True, blank=True)
    pec    = models.CharField(max_length=80, null=True, blank=True)
    email  = models.CharField(max_length=40, null=True, blank=True)
    sito   = models.CharField(max_length=40, null=True, blank=True)
    codfis = models.CharField(max_length=16, null=True, blank=True)
    pariva = models.CharField(max_length=11, null=True, blank=True)
    banapp = models.CharField(max_length=40, null=True, blank=True)
    fido   = models.IntegerField(null=True, blank=True)
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE, null=True, blank=True)
    codzon = models.ForeignKey(Zone, to_field='codzon', on_delete=models.CASCADE, null=True, blank=True)
    sconto = models.IntegerField(null=True, blank=True)
    codiva = models.ForeignKey(Ivaven, to_field='codiva', on_delete=models.CASCADE, null=True, blank=True)
    codese = models.ForeignKey(Eseiva, to_field='codese', on_delete=models.CASCADE, null=True, blank=True)
    codcab = models.CharField(max_length=5, null=True, blank=True)
    codabi = models.CharField(max_length=5, null=True, blank=True)
    codval = models.ForeignKey(Valute, to_field='codval', on_delete=models.CASCADE, null=True, blank=True)
    codnaz = models.ForeignKey(Nazion, to_field='codnaz', on_delete=models.CASCADE, null=True, blank=True)
    paese  = models.CharField(max_length=2, null=True, blank=True)
    cineur = models.CharField(max_length=2, null=True, blank=True)
    cin    = models.CharField(max_length=1, null=True, blank=True)
    conto  = models.CharField(max_length=12, null=True, blank=True)
    codcat = models.ForeignKey(Catego, to_field='codcat', on_delete=models.CASCADE, null=True, blank=True)
    chiusf = models.DateField(null=True, blank=True)
    chiust = models.DateField(null=True, blank=True)
    nome   = models.CharField(max_length=30, null=True, blank=True)
    spese  = models.BooleanField(default=False, null=True, blank=True)
    storic = models.BooleanField(default=False, null=True, blank=True)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE, null=True, blank=True)
    staest = models.CharField(max_length=3, null=True, blank=True)
    tipfor = models.IntegerField(null=True, blank=True)
    alias  = models.CharField(max_length=40, null=True, blank=True)
    spesom = models.BooleanField(default=False, null=True, blank=True)
    fatema = models.BooleanField(default=False, null=True, blank=True)
    impass = models.IntegerField(null=True, blank=True)
    annass = models.CharField(max_length=4, null=True, blank=True)
    coduni = models.CharField(max_length=7, null=True, blank=True)
    splpay = models.CharField(max_length=1, null=True, blank=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'client'
        managed = True

    def __str__(self):
        return f"{self.codcli} - {self.ragsoc}"
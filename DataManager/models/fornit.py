from django.db import models
from Login.models import CustomUser
from DataManager.models.banche import Banche
from DataManager.models.nazion import Nazion
from DataManager.models.catego import Catego
from DataManager.models.modpag import Modpag
from DataManager.models.ivaacq import Ivaacq
from DataManager.models.zone import Zone

class Fornit(models.Model):
    ragsoc = models.CharField(unique=True, max_length=40)
    datagg = models.CharField(max_length=40, null=True, blank=True)
    indiri = models.CharField(max_length=40, null=True, blank=True)
    locali = models.CharField(max_length=30, null=True, blank=True)
    provin = models.CharField(max_length=2, null=True, blank=True)
    cap    = models.CharField(max_length=5, null=True, blank=True)
    codfis = models.CharField(max_length=5, null=True, blank=True)
    pariva = models.CharField(max_length=15, null=True, blank=True)
    telef1 = models.CharField(max_length=15, null=True, blank=True)
    telef2 = models.CharField(max_length=15, null=True, blank=True)
    cellul = models.CharField(max_length=15, null=True, blank=True)
    fax    = models.CharField(max_length=15, null=True, blank=True)
    email  = models.CharField(max_length=40, null=True, blank=True)
    codfor = models.CharField(primary_key=True, max_length=5)
    sito   = models.CharField(max_length=40, null=True, blank=True)
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE, null=True, blank=True)
    pae    = models.CharField(max_length=2, null=True, blank=True)
    cineur = models.CharField(max_length=2, null=True, blank=True)
    cin    = models.CharField(max_length=1, null=True, blank=True)
    conto  = models.CharField(max_length=12, null=True, blank=True)
    codabi = models.CharField(max_length=5, null=True, blank=True)
    codcab = models.CharField(max_length=5, null=True, blank=True)
    banapp = models.CharField(max_length=40, null=True, blank=True)
    codnaz = models.ForeignKey(Nazion, to_field='codnaz', on_delete=models.CASCADE, null=True, blank=True)
    codiva = models.ForeignKey(Ivaacq, to_field='codiva', on_delete=models.CASCADE, null=True, blank=True)
    codcat = models.ForeignKey(Catego, to_field='codcat', on_delete=models.CASCADE, null=True, blank=True)
    codzon = models.ForeignKey(Zone, to_field='codzon', on_delete=models.CASCADE, null=True, blank=True)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE, null=True, blank=True)
    storic = models.BooleanField()
    staest = models.CharField(max_length=3, null=True, blank=True)
    tipfor = models.IntegerField(null=True, blank=True)
    spesom = models.BooleanField()
    schcar = models.BooleanField()
    alias  = models.CharField(max_length=24, null=True, blank=True)
    regfis = models.CharField(max_length=4, null=True, blank=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True
        db_table = 'fornit'
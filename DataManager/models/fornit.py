from django.db import models
from Login.models import CustomUser
from datetime import datetime
from DataManager.models.banche import Banche
from DataManager.models.nazion import Nazion
from DataManager.models.catego import Catego
from DataManager.models.modpag import Modpag
from DataManager.models.ivaacq import Ivaacq
from DataManager.models.zone import Zone

class Fornit(models.Model):
    ragsoc = models.CharField(unique=True, max_length=40)
    datagg = models.CharField(max_length=40)
    indiri = models.CharField(max_length=40)
    locali = models.CharField(max_length=30)
    provin = models.CharField(max_length=2)
    cap    = models.CharField(max_length=5)
    codfis = models.CharField(max_length=5)
    pariva = models.CharField(max_length=15)
    telef1 = models.CharField(max_length=15)
    telef2 = models.CharField(max_length=15)
    cellul = models.CharField(max_length=15)
    fax    = models.CharField(max_length=15)
    email  = models.CharField(max_length=40)
    codfor = models.CharField(primary_key=True, max_length=5)
    sito   = models.CharField(max_length=40)
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE)
    pae    = models.CharField(max_length=2)
    cineur = models.CharField(max_length=2)
    cin    = models.CharField(max_length=1)
    conto  = models.CharField(max_length=12)
    codabi = models.CharField(max_length=5)
    codcab = models.CharField(max_length=5)
    banapp = models.CharField(max_length=40)
    codnaz = models.ForeignKey(Nazion, to_field='codnaz', on_delete=models.CASCADE)
    codiva = models.ForeignKey(Ivaacq, to_field='codiva', on_delete=models.CASCADE)
    codcat = models.ForeignKey(Catego, to_field='codcat', on_delete=models.CASCADE)
    codzon = models.ForeignKey(Zone, to_field='codzon', on_delete=models.CASCADE)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE)
    storic = models.BooleanField()
    staest = models.CharField(max_length=3)
    tipfor = models.IntegerField()
    spesom = models.BooleanField()
    schcar = models.BooleanField()
    alias  = models.CharField(max_length=24)
    regfis = models.CharField(max_length=4)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)


    class Meta:
        managed = True
        db_table = 'fornit'
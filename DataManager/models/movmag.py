from django.db import models
from Login.models import CustomUser
from .artico import Artico
from .client import Client
from .fornit import Fornit
from .caumag import Caumag
from .ordfor import Ordfor
from .ordcli import Ordcli
from .ordpro import Ordpro
from .fasi import Fasi
from .commes import Commes
from Infinito.settings import DECVAL, DECPRE, DECQUA

class Movmag(models.Model):
    numpro = models.IntegerField()
    datmov = models.DateField()
    anno = models.IntegerField()
    numdoc = models.CharField(max_length=15, null=True, blank=True)
    codart = models.ForeignKey(Artico, to_field='codart', on_delete=models.CASCADE)
    codcau = models.ForeignKey(Caumag, to_field='codcau', on_delete=models.CASCADE, null=True, blank=True)
    quanti = models.DecimalField(max_digits=13, decimal_places=DECQUA)
    prezzo = models.DecimalField(max_digits=13, decimal_places=DECPRE, null=True, blank=True)
    valore = models.DecimalField(max_digits=13, decimal_places=DECVAL, null=True, blank=True)
    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE, null=True, blank=True)
    codfor = models.ForeignKey(Fornit, to_field='codfor', on_delete=models.CASCADE, null=True, blank=True)
    idorfo = models.ForeignKey(Ordfor, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    idorcl = models.ForeignKey(Ordcli, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    idorpr = models.ForeignKey(Ordpro, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    note   = models.CharField(max_length=50, null=True, blank=True)
    quamod = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapre = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    stato  = models.BooleanField()
    matric = models.CharField(max_length=8, null=True, blank=True)
    numrig = models.IntegerField(null=True, blank=True)
    modula = models.BooleanField()
    quakg  = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    ordsal = models.CharField(max_length=1, null=True, blank=True)
    numfat = models.CharField(max_length=15, null=True, blank=True)
    datfat = models.DateField(null=True, blank=True)
    noncon = models.BooleanField()
    codfas = models.ForeignKey(Fasi, to_field='codfas', on_delete=models.CASCADE, null=True, blank=True)
    numddt = models.IntegerField(null=True, blank=True)
    annddt = models.IntegerField(null=True, blank=True)
    codco1 = models.ForeignKey(Commes, to_field='codcom', on_delete=models.CASCADE, null=True, blank=True, related_name='codco1')
    codco2 = models.ForeignKey(Commes, to_field='codcom', on_delete=models.CASCADE, null=True, blank=True, related_name='codco2')
    codco3 = models.ForeignKey(Commes, to_field='codcom', on_delete=models.CASCADE, null=True, blank=True, related_name='codco3')
    codco4 = models.ForeignKey(Commes, to_field='codcom', on_delete=models.CASCADE, null=True, blank=True, related_name='codco4')
    codco5 = models.ForeignKey(Commes, to_field='codcom', on_delete=models.CASCADE, null=True, blank=True, related_name='codco5')
    quaco1 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quaco2 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quaco3 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quaco4 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quaco5 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapr1 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapr2 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapr3 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapr4 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    quapr5 = models.DecimalField(max_digits=13, decimal_places=DECQUA, null=True, blank=True)
    contro = models.BooleanField()
    tipdoc = models.CharField(max_length=2, null=True, blank=True) 

    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['numpro', 'anno'], name='movmag_sk')
        ]
        managed = True
        db_table = 'movmag'
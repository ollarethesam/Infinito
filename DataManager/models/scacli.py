from django.db import models
from Login.models import CustomUser
from .client import Client
from .valute import Valute
from .modpag import Modpag
from .banche import Banche

class Scacli(models.Model):
    numpro = models.IntegerField(auto_created=True, primary_key=True)
    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE)
    tipdoc = models.CharField(max_length=1)
    datdoc = models.DateField()
    numfat = models.CharField(max_length=5)
    descri = models.CharField(max_length=35)
    impfat = models.DecimalField(max_digits=11, decimal_places=2)
    imppag = models.DecimalField(max_digits=11, decimal_places=2)
    codval = models.ForeignKey(Valute, to_field='codval', on_delete=models.CASCADE, blank=True, null=True)
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE, blank=True, null=True)
    modpag = models.CharField(max_length=4, blank=True, null=True)
    cambio = models.DecimalField(max_digits=11, decimal_places=3)
    datsca = models.DateField()
    pagato = models.CharField(max_length=1)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE, blank=True, null=True)
    tippag = models.CharField(max_length=1)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'scacli'
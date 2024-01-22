from django.db import models
from Login.models import CustomUser
from .client import Client
from .valute import Valute
from .modpag import Modpag
from .banche import Banche

class Scacli(models.Model):
    numpro = models.AutoField(primary_key=True)
    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE)
    tipdoc = models.CharField(max_length=1)
    datdoc = models.DateTimeField()
    numfat = models.CharField(max_length=5)
    descri = models.CharField(max_length=35)
    impfat = models.DecimalField(max_digits=11, decimal_places=2)
    imppag = models.DecimalField(max_digits=11, decimal_places=2)
    codval = models.ForeignKey(Valute, to_field='codval', on_delete=models.CASCADE)
    codpag = models.ForeignKey(Modpag, to_field='codpag', on_delete=models.CASCADE)
    cambio = models.DecimalField(max_digits=11, decimal_places=3)
    datsca = models.DateTimeField()
    pagato = models.CharField(max_length=1)
    codban = models.ForeignKey(Banche, to_field='codban', on_delete=models.CASCADE)
    tippag = models.CharField(max_length=1)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'scaden'
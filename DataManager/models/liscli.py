from django.db import models
from Login.models import CustomUser
from .client import Client
from .artico import Artico
from Infinito.settings import DECVAL, DECPRE, DECQUA

class Liscli(models.Model):
    id = models.AutoField(primary_key=True)
    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE)
    codart = models.ForeignKey(Artico, to_field='codart', on_delete=models.CASCADE)
    prezzo = models.DecimalField(max_digits=13, decimal_places=DECPRE)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['codart', 'codcli'], name='liscli_sk')
        ]
        managed = True
        db_table = 'liscli'
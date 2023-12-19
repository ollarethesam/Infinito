from django.db import models
from django.contrib.auth.models import User
from viewflow.fields import CompositeKey
from .client import Client
from .artico import Artico
from datetime import datetime

class Liscli(models.Model):
    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE)
    codart = models.ForeignKey(Artico, to_field='codart', on_delete=models.CASCADE)
    prezzo = models.CharField(max_length=13)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)
    codcli_codart = CompositeKey(columns=['codcli', 'codart'])
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['codart', 'codcli'], name='liscli_sk'
            )
        ]
        managed = True
        db_table = 'liscli'
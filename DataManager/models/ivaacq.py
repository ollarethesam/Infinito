from django.db import models
from Login.models import CustomUser
from datetime import datetime

class Ivaacq(models.Model):
    codiva = models.CharField(max_length=2, primary_key=True)
    desiva = models.CharField(max_length=20)
    aliquo = models.FloatField()
    indetr = models.CharField(max_length=3)
    indagg = models.CharField(max_length=1)
    natura = models.CharField(max_length=2)
    esclip = models.BooleanField()
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'ivaacq'
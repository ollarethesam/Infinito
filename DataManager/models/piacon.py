from django.db import models
from Login.models import CustomUser
from datetime import datetime
from .conabi import Conabi

class Piacon(models.Model):
    codpia = models.CharField(primary_key=True, max_length=9)
    despia = models.CharField(max_length=100)
    codcon = models.ForeignKey(Conabi, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'piacon'
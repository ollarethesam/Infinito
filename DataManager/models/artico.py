from django.db import models
from Login.models import CustomUser
from datetime import datetime

class Artico(models.Model):
    codart = models.CharField(primary_key=True, max_length=20)
    desart = models.CharField(max_length=40)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'artico'
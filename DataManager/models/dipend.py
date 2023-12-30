from django.db import models
from Login.models import CustomUser
from datetime import datetime

class Dipend(models.Model):
    coddip = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    assunt = models.CharField(max_length=2)
    tiptar = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'dipend'
from django.db import models
from Login.models import CustomUser

class Caumag(models.Model):
    codcau = models.CharField(max_length=2, primary_key=True)
    descau = models.CharField(max_length=40)
    abbrev = models.CharField(max_length=13)
    azione = models.CharField(max_length=1)
    appart = models.CharField(max_length=1)
    gesord = models.BooleanField()
    valori = models.BooleanField()

    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'caumag'
from django.db import models
from Login.models import CustomUser

class Ivacor(models.Model):
    codiva = models.CharField(max_length=2, primary_key=True)
    desiva = models.CharField(max_length=20)
    aliquo = models.FloatField()
    natura = models.CharField(max_length=2)
    esclip = models.BooleanField()
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'ivacor'
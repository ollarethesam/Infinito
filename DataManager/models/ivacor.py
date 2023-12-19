from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Ivacor(models.Model):
    codiva = models.CharField(max_length=2, primary_key=True)
    desiva = models.CharField(max_length=20)
    aliquo = models.FloatField()
    natura = models.CharField(max_length=2)
    esclip = models.BooleanField()
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'ivacor'
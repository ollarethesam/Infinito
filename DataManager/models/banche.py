from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Banche(models.Model):
    codban = models.CharField(max_length=3, primary_key=True)
    desban = models.CharField(max_length=40, unique=True)
    codabi = models.CharField(max_length=5)
    codcab = models.CharField(max_length=5)
    codsia = models.CharField(max_length=5)
    iban = models.CharField(max_length=27)
    bic = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'banche'

    def __str__(self):
        return f"{self.codban} - {self.desban}"
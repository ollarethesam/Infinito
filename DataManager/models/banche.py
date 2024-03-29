from django.db import models
from Login.models import CustomUser

class Banche(models.Model):
    codban = models.CharField(max_length=3, primary_key=True)
    desban = models.CharField(max_length=40, unique=True)
    codabi = models.CharField(max_length=5)
    codcab = models.CharField(max_length=5)
    codsia = models.CharField(max_length=5)
    iban = models.CharField(max_length=27)
    bic = models.CharField(max_length=11)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banche'
        managed = True

    def __str__(self):
        return f"{self.codban} - {self.desban}"
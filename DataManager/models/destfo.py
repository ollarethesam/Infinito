from django.db import models
from Login.models import CustomUser
from .fornit import Fornit

class Destfo(models.Model):
    codfor = models.ForeignKey(Fornit, to_field='codfor', on_delete=models.CASCADE)
    codest = models.CharField(max_length=5, primary_key=True)
    dedest = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'destfo'
from django.db import models
from .client import Client
from Login.models import CustomUser

class Destcl(models.Model):

    codcli = models.ForeignKey(Client, to_field='codcli', on_delete=models.CASCADE)
    codest = models.CharField(max_length=5, primary_key=True)
    dedest = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'destcl'
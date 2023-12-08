from django.db import models
from django.contrib.auth.models import User
from .fornit import Fornit
from datetime import datetime

class Destfo(models.Model):
    codfor = models.ForeignKey(Fornit, to_field='codfor', on_delete=models.CASCADE)
    codest = models.CharField(max_length=5, primary_key=True)
    dedest = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'destfo'
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Dipend(models.Model):
    coddip = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    assunt = models.CharField(max_length=2)
    tiptar = models.CharField(max_length=30)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'dipend'
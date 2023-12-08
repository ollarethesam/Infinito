from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Artico(models.Model):
    codart = models.CharField(primary_key=True, max_length=20)
    desart = models.CharField(max_length=40)
    prezzo = models.CharField(max_length=15)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'artico'
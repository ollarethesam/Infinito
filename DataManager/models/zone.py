from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Zone(models.Model):
    codzon = models.CharField(max_length=3, primary_key=True)
    deszon = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'zone'
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Cenlav(models.Model):
    codcen = models.CharField(max_length=4, primary_key=True)
    descen = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'cenlav'
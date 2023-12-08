from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Valute(models.Model):
    codval = models.CharField(primary_key=True, max_length=3)
    desval = models.CharField(max_length=50)
    simval = models.CharField(max_length=2)
    valcam = models.CharField(max_length=30)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'valute'
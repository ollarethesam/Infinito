from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Modpag(models.Model):
    codpag = models.CharField(max_length=3, primary_key=True)
    despag = models.CharField(max_length=40, unique=True)
    tippag = models.CharField(max_length=40)
    numrat = models.CharField(max_length=3)
    giosca = models.CharField(max_length=3)
    period = models.CharField(max_length=3)
    tipsca = models.CharField(max_length=40)
    escmes = models.CharField(max_length=40)
    scocas = models.CharField(max_length=5)
    gifisc = models.CharField(max_length=3)
    modpag = models.CharField(max_length=11)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'modpag'
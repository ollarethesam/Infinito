from django.db import models
from Login.models import CustomUser

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
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'modpag'
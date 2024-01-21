from django.db import models
from Login.models import CustomUser

class Valute(models.Model):
    codval = models.CharField(primary_key=True, max_length=3)
    desval = models.CharField(max_length=50)
    simval = models.CharField(max_length=2)
    valcam = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'valute'
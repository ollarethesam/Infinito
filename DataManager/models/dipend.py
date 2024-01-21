from django.db import models
from Login.models import CustomUser

class Dipend(models.Model):
    coddip = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    assunt = models.CharField(max_length=2)
    tiptar = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'dipend'
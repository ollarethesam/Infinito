from django.db import models
from Login.models import CustomUser

class Cenlav(models.Model):
    codcen = models.CharField(max_length=4, primary_key=True)
    descen = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'cenlav'
from django.db import models
from Login.models import CustomUser

class Conabi(models.Model):
    codcon = models.CharField(primary_key=True, max_length=20)
    descon = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'conabi'
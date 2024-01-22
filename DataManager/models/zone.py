from django.db import models
from Login.models import CustomUser

class Zone(models.Model):
    codzon = models.CharField(max_length=3, primary_key=True)
    deszon = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'zone'
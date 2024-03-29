from django.db import models
from Login.models import CustomUser

class Spediz(models.Model):
    codspe = models.CharField(max_length=3, primary_key=True)
    desspe = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'spediz'
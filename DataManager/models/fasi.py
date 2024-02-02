from django.db import models
from Login.models import CustomUser

class Fasi(models.Model):
    codfas = models.CharField(max_length=10)
    desfas = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'fasi'
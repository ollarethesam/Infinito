from django.db import models
from Login.models import CustomUser

class Commes(models.Model):
    codcom = models.CharField(max_length=10)
    desdes = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'commes'
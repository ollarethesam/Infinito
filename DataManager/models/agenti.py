from django.db import models
from Login.models import CustomUser

class Agenti(models.Model):
    codage = models.CharField(primary_key=True, max_length=3)
    desage = models.CharField(max_length=40)
    provvi = models.CharField(max_length=5)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True
        db_table = 'agenti'
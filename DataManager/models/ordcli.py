from django.db import models
from Login.models import CustomUser

class Ordcli(models.Model):
    id = models.AutoField(primary_key=True)
    nuorcl = models.CharField(max_length=10)
    anorcl = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nuorcl', 'anorcl'], name='ordcli_sk')
        ]
        managed = True
        db_table = 'ordcli'
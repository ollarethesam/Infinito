from django.db import models
from Login.models import CustomUser

class Ordcli(models.Model):
    nuorcl = models.CharField(max_length=10)
    anorcl = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nuorfo', 'anorfo'], name='ordcli_sk')
        ]
        managed = True
        db_table = 'ordcli'
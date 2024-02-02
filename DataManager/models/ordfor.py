from django.db import models
from Login.models import CustomUser

class Ordfor(models.Model):
    nuorfo = models.CharField(max_length=10)
    anorfo = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nuorfo', 'anorfo'], name='ordfor_sk')
        ]
        managed = True
        db_table = 'ordfor'
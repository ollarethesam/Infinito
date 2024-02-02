from django.db import models
from Login.models import CustomUser

class Ordpro(models.Model):
    nuorpr = models.CharField(max_length=10)
    anorpr = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nuorpr', 'anorpr'], name='ordpro_sk')
        ]
        managed = True
        db_table = 'ordpro'
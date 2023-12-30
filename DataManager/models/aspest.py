from django.db import models
from Login.models import CustomUser
from datetime import datetime

class Aspest(models.Model):
    codasp = models.CharField(primary_key=True, max_length=3)
    desasp = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'aspest'
from django.db import models
from Login.models import CustomUser

class Aspest(models.Model):
    codasp = models.CharField(primary_key=True, max_length=3)
    desasp = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'aspest'
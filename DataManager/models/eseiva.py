from django.db import models
from Login.models import CustomUser

class Eseiva(models.Model):
    codese = models.CharField(max_length=4, primary_key=True)
    riccli = models.CharField(max_length=4)
    datric = models.DateField()
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'eseiva'
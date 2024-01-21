from django.db import models
from Login.models import CustomUser


class Tipall(models.Model):
    codtal = models.CharField(primary_key=True, max_length=3)
    destal = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'tipall'
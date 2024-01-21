from django.db import models
from Login.models import CustomUser
from .piacon import Piacon

class Catcon(models.Model):
    codcat = models.CharField(max_length=3, primary_key=True)
    descat = models.CharField(max_length=50, unique=True)
    codpia = models.ForeignKey(Piacon, to_field='codpia', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)

    class Meta:
        managed = True
        db_table = 'catcon'
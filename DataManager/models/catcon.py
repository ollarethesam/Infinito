from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .piacon import Piacon

class Catcon(models.Model):
    codcat = models.CharField(max_length=3, primary_key=True)
    descat = models.CharField(max_length=50, unique=True)
    codpia = models.ForeignKey(Piacon, to_field='codpia', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'catcon'
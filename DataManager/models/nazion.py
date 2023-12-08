from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Nazion(models.Model):
    codnaz = models.CharField(primary_key=True, max_length=2)
    desnaz = models.CharField(max_length=50)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'nazion'
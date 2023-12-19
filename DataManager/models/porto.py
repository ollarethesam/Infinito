from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Porto(models.Model):
    codpor = models.CharField(primary_key=True, max_length=3)
    despor = models.CharField(max_length=50)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now().replace(microsecond=0), editable=False)

    class Meta:
        managed = True
        db_table = 'porto'
from django.db import models
from Login.models import CustomUser

class Catego(models.Model):
    codcat = models.CharField(primary_key=True, max_length=2)
    descat = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'catego'
        managed = True

    def __str__(self):
        return f"{self.codcat} - {self.descat}"
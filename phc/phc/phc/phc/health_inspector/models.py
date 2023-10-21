from django.db import models

# Create your models here.

class HealthInspector(models.Model):
    hi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    email = models.CharField(max_length=233)
    phone = models.CharField(max_length=12)
    age = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'health_inspector'


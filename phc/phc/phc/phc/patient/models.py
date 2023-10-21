from django.db import models

# Create your models here.

class Patient(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=12)
    gender = models.CharField(max_length=23)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'patient'


from django.db import models

# Create your models here.

class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=33)
    name = models.CharField(max_length=333)
    address = models.CharField(max_length=333)
    mail = models.CharField(max_length=45)
    phone = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'lab'


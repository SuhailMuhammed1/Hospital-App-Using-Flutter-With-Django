from django.db import models

# Create your models here.
class Doctor(models.Model):
    dr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    age = models.CharField(max_length=12)
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=22)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doctor'


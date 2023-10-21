from django.db import models
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.

class Appointment(models.Model):
    app_id = models.AutoField(primary_key=True)
    # dr_id = models.IntegerField()
    dr=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # p_id = models.IntegerField()
    p=models.ForeignKey(Patient,on_delete=models.CASCADE)
    status = models.CharField(max_length=23)
    date = models.DateField()
    time = models.CharField(max_length=23)
    sc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'appointment'


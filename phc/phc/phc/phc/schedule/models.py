from django.db import models

# Create your models here.
class Schedule(models.Model):
    sc_id = models.AutoField(primary_key=True)
    dr_id = models.IntegerField()
    time = models.TimeField()
    day = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'schedule'

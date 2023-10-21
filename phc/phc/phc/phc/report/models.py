from django.db import models

# Create your models here.
class Report(models.Model):
    r_id = models.AutoField(primary_key=True)
    p_id = models.IntegerField()
    lab_id = models.IntegerField()
    records = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report'

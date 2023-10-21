from django.db import models

# Create your models here.

class Massege(models.Model):
    msg_id = models.AutoField(primary_key=True)
    # hi_id = models.IntegerField()
    # p_id = models.IntegerField()
    message: str = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'massege'


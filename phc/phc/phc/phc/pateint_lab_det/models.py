from django.db import models

# Create your models here.

class PateintLabDet(models.Model):
    pld_id = models.AutoField(primary_key=True)
    p_id = models.IntegerField()
    lab_id = models.IntegerField()
    lab_detials = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'pateint_lab_det'

class LabReport(models.Model):
    lb_id = models.AutoField(primary_key=True)
    heamoglobin = models.CharField(max_length=45)
    total_wbc_count = models.CharField(max_length=45)
    dc_neutrophil = models.CharField(max_length=45)
    lymphocyte = models.CharField(max_length=45)
    eosinophil = models.CharField(max_length=45)
    basophil = models.CharField(max_length=45)
    monocyte = models.CharField(max_length=45)
    esr = models.CharField(max_length=45)
    platelet_count = models.CharField(max_length=45)
    malarial_parasite = models.CharField(max_length=45)
    albumin = models.CharField(max_length=45)
    albumin1 = models.CharField(max_length=45)
    sugar = models.CharField(max_length=45)
    microscopy = models.CharField(max_length=45)
    pusceils = models.CharField(max_length=45)
    rbcs = models.CharField(max_length=45)
    fbs = models.CharField(max_length=45)
    rbs = models.CharField(max_length=45)
    ppbs = models.CharField(max_length=45)
    hba1c = models.CharField(max_length=45)
    t_cholestrol = models.CharField(db_column='t.cholestrol', max_length=45)  # Field renamed to remove unsuitable characters.
    triglycerides = models.CharField(max_length=45)
    hdl = models.CharField(max_length=45)
    ldl = models.CharField(max_length=45)
    vldl = models.CharField(max_length=45)
    tbirirubin = models.CharField(max_length=45)
    dbilirubin = models.CharField(max_length=45)
    sgot = models.CharField(max_length=45)
    sgpt = models.CharField(max_length=45)
    epithelial = models.CharField(max_length=45)
    crystal = models.CharField(max_length=45)
    casts = models.CharField(max_length=45)
    lab_reportcol = models.CharField(max_length=45)
    bacteria = models.CharField(max_length=45)
    bile_salt = models.CharField(max_length=45)
    bile_pigment = models.CharField(max_length=45)
    stool = models.CharField(max_length=45)
    sputum = models.CharField(max_length=45)
    sodium = models.CharField(max_length=45)
    potassium = models.CharField(max_length=45)
    tprotien = models.CharField(max_length=45)
    globulin = models.CharField(max_length=45)
    ag_ratio = models.CharField(max_length=45)
    alakine_phos = models.CharField(max_length=45)
    urea = models.CharField(max_length=45)
    screat = models.CharField(max_length=45)
    suricacid = models.CharField(max_length=45)
    hiv = models.CharField(max_length=45)
    hbsag = models.CharField(max_length=45)
    rdt = models.CharField(max_length=45)
    dengue = models.CharField(max_length=45)
    ns1ag = models.CharField(max_length=45)
    lgg1gm = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    uid = models.CharField(max_length=45)







    class Meta:
        managed = False
        db_table = 'lab_report'

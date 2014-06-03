from django.db import models

# Create your models here.
class WaterT(models.Model):
    surf_temp = models.IntegerField()
    meas_date = models.DateTimeField()

class WaterQuality(models.Model):
    ecoli = models.IntegerField()

class AirT(models.Model):
    air_temp = models.IntegerField()
from django.db import models

# Create your models here.
class WaterT(models.Model):
    surf_temp = models.IntegerField()
    meas_date = models.DateTimeField()
    def __unicode__(self):
        return self.surf_temp

# class WaterQuality(models.Model):
#     ecoli = models.IntegerField()
#     def __unicode__(self):
#         return self.ecoli

# class AirT(models.Model):
#     air_temp = models.IntegerField()
#     def __unicode__(self):
#         return self.air_temp
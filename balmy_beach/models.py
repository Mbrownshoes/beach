from django.db import models
from datetime import datetime
# Create your models here.
class AirT(models.Model):
    air_temp = models.IntegerField()
    def __unicode__(self):
        return unicode(self.air_temp)

class WaterT(models.Model):
    # airt = models.ForeignKey(AirT)
    surf_temp = models.IntegerField()
    meas_date = models.DateTimeField(default=datetime.now, blank=True)
    def __unicode__(self):
        return unicode(self.surf_temp)

class WaterQuality(models.Model):
    ecoli = models.IntegerField()
    def __unicode__(self):
        return unicode(self.ecoli)


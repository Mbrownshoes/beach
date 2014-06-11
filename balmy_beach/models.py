from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class WaterT(models.Model):
    # airt = models.ForeignKey(AirT)
    surf_temp = models.IntegerField()
    def __unicode__(self):
        return unicode(self.surf_temp)

class AirT(models.Model):
    air_temp = models.IntegerField()
    # watert = models.ForeignKey(WaterT)
    pub_date = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return unicode(self.air_temp)

class WaterQuality(models.Model):
    ecoli = models.IntegerField()
    def __unicode__(self):
        return unicode(self.ecoli)


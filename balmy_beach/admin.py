from django.contrib import admin
from balmy_beach.models import AirT, WaterT, WaterQuality
# Register your models here.

admin.site.register(AirT)
admin.site.register(WaterT)
admin.site.register(WaterQuality)
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item
from scrapy.contrib.djangoitem import DjangoItem

from balmy_beach.models import WaterT, WaterQuality, AirT

class WaterTItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = WaterT

class WaterQualityItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = WaterQuality

class AirTItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = AirT    
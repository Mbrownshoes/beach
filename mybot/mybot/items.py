# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field
from scrapy.contrib.djangoitem import DjangoItem

from balmy_beach.models import WaterT

class WaterTItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = WaterT

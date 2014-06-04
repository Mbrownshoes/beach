# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from balmy_beach.models import AirT, WaterT


class MybotPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

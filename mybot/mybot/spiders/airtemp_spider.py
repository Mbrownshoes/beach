from scrapy.spider import Spider
from scrapy.selector import Selector
from mybot.items import AirTItem, WaterTItem
import re

class AirTSpider(Spider):
    name = 'airtemp'
    allowed_domains = ['weather.gc.ca']
    start_urls = [
    "http://weather.gc.ca/marine/weatherConditions-currentConditions_e.html?mapID=11&siteID=08207&stationID=YTZ",
    ]

    def parse(self, response):
        sel = Selector(response)    

        sites  =sel.xpath('//table[@class="wc-table"]').re(r'Air temperature.+\s.+')
        items=[]
        for site in sites:
            item=AirTItem()
            m = re.search('<td>(\w+)', site)
            item['air_temp'] = m.group(1)
 
       
        yield item

      

class WaterTSpider(Spider):
    name = 'watertemp'
    allowed_domains = ['weather.gc.ca']
    start_urls = [
    "http://weather.gc.ca/marine/weatherConditions-currentConditions_e.html?mapID=11&siteID=08207&stationID=45159"
    ]
    
    def parse(self, response):
        sel = Selector(response)   
       
        sites  =sel.xpath('//table[@class="wc-table"]').re(r'Water temperature.+\s.+')
        items=[]
        for site in sites:
            item=WaterTItem()
            m = re.search('<td>(\w+)', site)
            item['surf_temp'] = m.group(1)
        yield item
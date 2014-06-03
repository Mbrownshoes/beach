from scrapy.spider import Spider
from scrapy.selector import Selector
# from mybot.items import WaterTItem
import re

class WaterTSpider(Spider):
    name = 'watert'
    allowed_domains = ['weather.gc.ca']
    start_urls = [
    "http://weather.gc.ca/marine/weatherConditions-currentConditions_e.html?mapID=11&siteID=08207&stationID=YTZ"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites  =sel.xpath('//table[@class="wc-table"]').re(r'Air temperature.+\s.+')
        for site in sites:
            m = re.search('<td>(\w+)', site)

        # for site in sites:
        #     Ta = site.xpath().re(r'Air temperature".+<td>..</td>')
       
        print m.group(1)



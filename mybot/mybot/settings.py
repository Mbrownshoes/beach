# Scrapy settings for mybot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
sys.path.append('/Users/mathewbrown/projects/beach')

#Setting up django's settings module name.

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'beach.settings'
BOT_NAME = 'mybot'

SPIDER_MODULES = ['mybot.spiders']
NEWSPIDER_MODULE = 'mybot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mybot (+http://www.yourdomain.com)'
#setting up django's project full path.
ITEM_PIPELINES = {
    'mybot.pipelines.MybotPipeline': 1000,
}
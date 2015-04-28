# -*- coding: utf-8 -*-

# Scrapy settings for bahaCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bahaCrawler'

SPIDER_MODULES = ['bahaCrawler.spiders']
NEWSPIDER_MODULE = 'bahaCrawler.spiders'

BOT_NAME = 'baha'
SPIDER_MODULES = ['bahaCrawler']
NEWSPIDER_MODULE = 'baha.spiders'
USER_AGENT = "Chrome/40.0.2214.111"
DOWNLOAD_DELAY = 0.25
	#LOG_FILE = 'log.txt'

FEED_URI = 'export.json'
FEED_FORMAT = 'json'
FEED_EXPORTERS = {
   'json': 'bahaCrawler.pipelines.UnicodeJsonItemExporter'
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bahaCrawler (+http://www.yourdomain.com)'

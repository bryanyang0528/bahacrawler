# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class BahaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 	title = Field()
 	rank = Field()
 	hot = Field()
 	lauch_day = Field()
 	spider = Field()


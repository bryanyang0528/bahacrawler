import sys
import scrapy
from datetime import datetime
from scrapy.http import Request, FormRequest, TextResponse
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ..items import BahaCrawlerItem

class BahaNotLaunch(Spider):
	
	name = "bahaNotLaunch"
	allowed_domains = ["com.tw"]
	start_urls = ["http://acg.gamer.com.tw/index.php?p=ANDROID&t=2&"]

	def parse(self, response):
		yield Request("http://acg.gamer.com.tw/index.php?p=ANDROID&t=2&", cookies={
			'ckACGSHOWTYPE':'L'}, callback = self.parse_table )

	def parse_table(self, response):
		
		items = []
		sel = Selector(response)
		tables = sel.xpath('//table[@class="BH-table ACG-table1"]/tr')

		
		for table in tables:
			if table == tables[0]:
				pass
			else:
				item = BahaCrawlerItem()
				item['spider'] = "bahaNotLaunch"
				item['title'] = table.xpath('.//td[@class="ACG-tb1left"]/a/text()')[0].extract()
				item['hot'] = table.xpath('.//td/text()')[3].extract()
				item['lauch_day'] = table.xpath('.//td/text()')[1].extract()

				items.append(item)
				
		return items
		

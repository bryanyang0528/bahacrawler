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

class BahaRancking(Spider):
	
	name = "bahaRanking"
	allowed_domains = ["gov.tw"]
	start_urls = [
		"http://forum.gamer.com.tw/rank.php?c=30"
	]

	def parse(self, response):
		
		items = []
		sel = Selector(response)
		tables = sel.xpath('//table[@class="BH-table BH-table1"]/tr')
		#print tables[1].extract()

		for table in tables:
			
			item = BahaCrawlerItem()
			item['spider'] = "bahaRanking"
			item['title'] = table.xpath('.//td/h1/a/text()').extract()
			item['rank'] = table.xpath('.//td[@width="35"]/text()').extract()

			items.append(item)
			
		return items
		

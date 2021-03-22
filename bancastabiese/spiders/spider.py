import scrapy

from scrapy.loader import ItemLoader
from ..items import BancastabieseItem
from itemloaders.processors import TakeFirst


class BancastabieseSpider(scrapy.Spider):
	name = 'bancastabiese'
	start_urls = ['http://www.bancastabiese.it/News.aspx']

	def parse(self, response):
		post_links = response.xpath('//ul[@class="list-of-links"]//a/@href').getall()
		for link in post_links:
			if link[-3:] == 'spx':
				yield response.follow(link, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1//text()[normalize-space()]').get()
		description = response.xpath('//div[contains(@id, "content-main-two-column")]//text()[normalize-space() and not(ancestor::h1)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BancastabieseItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()

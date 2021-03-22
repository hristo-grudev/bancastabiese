import scrapy


class BancastabieseItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()

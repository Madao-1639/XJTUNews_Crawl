import scrapy


class XjtunewsItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    source  = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()



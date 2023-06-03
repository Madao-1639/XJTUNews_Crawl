import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from XJTUNews.items import XjtunewsItem
import re

class NewsspiderSpider(CrawlSpider):
    name = 'newsSpider'
    allowed_domains = ['news.xjtu.edu.cn']
    start_urls = ['http://news.xjtu.edu.cn/zyxw.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://news.xjtu.edu.cn/zyxw/\d+.htm'),follow=True),
        Rule(LinkExtractor(allow=r'http://news.xjtu.edu.cn/info/\d+/\d+.htm'),callback='parse_news',follow=False)
    )


    def parse_news(self, response):
        _id = re.search(r'/(\d+).htm',response._url).group(1)
        info_box = response.xpath('//div[@class="con-tit"]')
        title_slices = info_box.xpath('./h1//text()').getall()
        if len(title_slices)>1:
            title='\n'.join(
                map(lambda s:s.strip(),title_slices)
            )
        else:
            title=title_slices[0].strip()
        info = info_box.xpath('.//div[@class="shfffff"]/span/text()').getall()
        for s in info:
            if s[:2] == '来源':
                source = s.strip()[3:]
            elif s[:2] == '日期':
                date = s[3:]
        content_slices = response.xpath('.//div[@class="conte fl"]/div[@id="vsb_content_2"]//text()').getall()
        content='\n'.join(
            filter(lambda s:len(s)>0, map(lambda s:s.strip(),content_slices))
        )
    
        yield XjtunewsItem(_id=_id,title=title,source=source,date=date,content=content)
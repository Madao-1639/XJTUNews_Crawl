from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class XjtunewsPipeline:
    def __init__(self):
        self.fp=open('News.csv','wb')
        self.exporter=CsvItemExporter(self.fp,encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

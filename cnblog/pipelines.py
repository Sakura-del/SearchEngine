# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import JsonLinesItemExporter

class CnblogPipeline(object):
    def process_item(self, item, spider):

        item.save_to_es()
        return item

# class JsonPipeline(object):
#     def __init__(self):
#         self.fp = open('cnblogs.json','wb')
#         self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.fp.write(b'[')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         self.fp.write(b',')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.write(b"]")
#         self.fp.close()

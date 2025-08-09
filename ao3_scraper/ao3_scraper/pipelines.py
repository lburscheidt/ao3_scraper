# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, datetime

class Ao3ScraperPipeline:
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        # converting item to dict above, since dumps only intakes dict.
        self.file.write(line)                    # writing content in output file.
        return item

    def open_spider(self, spider):
        self.file = open('result.json', 'w')

    def close_spider(self, spider):
        self.file.close()


class JsonWriterPipeline(object):
    def process_item(self, item, spider):
        # return item
        fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
        try:
            with open(fileName, "w") as fp:
                json.dump(dict(item), fp)
                return item
        except:
            return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        with open("../movies.csv", "a+", encoding='utf-8') as f:
            f.write(f"\"{item['name']}\",\"{item['tag']}\",\"{item['plan_date']}\"\n")
        return item

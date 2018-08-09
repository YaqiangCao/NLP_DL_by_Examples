# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import io
class WanfangPipeline(object):
    def __init__(self):
        self.count = 0
        self.paper = 0
    def process_item(self, item, spider):
        a = json.dumps(dict(item), ensure_ascii = False)
        if self.count % 10000 == 0:
            print("-------------------"*10)
            self.paper += 1
        with io.open("./data.txt", "a", encoding="utf-8"  ) as f:
            f.write(a+"\n")
            f.close()
        self.count += 1
        print(self.count,"**"*20)

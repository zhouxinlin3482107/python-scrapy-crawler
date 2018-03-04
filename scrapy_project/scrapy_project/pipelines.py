# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ScrapyProjectPipeline(object):


    def __init__(self):
        self.filename1 = 'result_data/lianjia.csv'
        self.filename2 = 'result_data/douban.csv'
        self.filename3 = 'result_data/loewe.csv'
        self.f = None

    def open_spider(self, spider):
        if spider.name == 'lianjia':
            self.f = open(self.filename1, 'w+', encoding='utf-8')
        if spider.name == 'douban':
            self.f = open(self.filename2, 'w+', encoding='utf-8')
        if spider.name == 'loewe':
            self.f = open(self.filename3, 'w+', encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        if spider.name == 'lianjia':
            url = item['url']
            title = item['title']
            unitPrice  = item['unitPrice']+'元'
            unitPrice2 = int(item['unitPrice'])
            area = item['area']
            area2 = float(area.replace('平米',''))
            totalPrice = item['totalPrice']+'万元'
            if (unitPrice2 <= 90000 and area2 >= 50):
                self.f.write('%s, %s, %s, %s, %s\n' % (url,title,unitPrice,area,totalPrice))
        elif spider.name == 'douban':
            title = item['title']
            number = item['number']
            self.f.write('%s, %s\n' % (title,number))
        elif spider.name == 'loewe':
            link_data = item['link_data']
            self.f.write('%s\n' % (link_data))
        else:
            return item


    

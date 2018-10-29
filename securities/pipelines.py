# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SecuritiesPipeline(object):
    def process_item(self, item, spider):

        f = open('executive_prep.csv', 'a', encoding='utf8')
        write = csv.writer(f)
        write.writerow((item['name'], item['sex'], item['age'], item['code'], item['jobs']))
        return item


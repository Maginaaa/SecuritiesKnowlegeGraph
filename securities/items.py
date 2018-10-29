# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class SecuritiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GetItem(scrapy.Item):
    name = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    code = scrapy.Field()
    jobs = scrapy.Field()
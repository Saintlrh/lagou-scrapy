# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    job = scrapy.Field()
    address = scrapy.Field()
    money = scrapy.Field()
    #request要求
    req = scrapy.Field()
    company = scrapy.Field()
    #qualification资质
    qua = scrapy.Field()
    des = scrapy.Field()

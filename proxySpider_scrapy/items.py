# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#
# class ProxyItem(scrapy.Item):
#     ip = scrapy.Field()  # ip
#     port = scrapy.Field()  # 端口
#

class MysqlItem(scrapy.Item):
    ip = scrapy.Field()  # ip
    port = scrapy.Field()  # 端口
    anonymity = scrapy.Field()  # 端口
    type = scrapy.Field()  # 端口
    alive_time = scrapy.Field()  # 端口
    final_verification_time = scrapy.Field()  # 端口
    warehousing_time = scrapy.Field()  # 端口

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

import pymysql
from scrapy.utils.project import get_project_settings

from proxySpider_scrapy.spiders.proxySpider import ProxySpider
from proxySpider_scrapy.utils.html_to_markdown import HTMLTOMARKDOWN


class MongoPipeline(object):
    proxyId = 1  # 设置一个ID号，方便多线程验证

    def process_item(self, item, spider):
        '''

        :param item:
        :param spider:
        :return:
        '''
        if spider.name == 'proxy':  # 需要判断是哪个爬虫

            proxySpider = ProxySpider(spider)
            proxy = {'ip': item['ip'], 'port': item['port']}
            proxy_all = {'ip': item['ip'], 'port': item['port'], 'proxyId': self.proxyId}
            if proxySpider.db_helper.insert(proxy, proxy_all) == True:
                self.proxyId += 1
            return item

        else:
            return item


class MysqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PWD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.name, use_unicode=True, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()

    def process_item(self, item, spider):
        insertSql = "insert into ip_pool_xicidaili(ip,port,anonymity,type,alive_time,final_verification_time) values (%s,%s,%s,%s,%s,%s)"

        param = (
            item['ip'], item['port'], item['anonymity'], item['type'], item['alive_time'],
            item['final_verification_time'])

        self.cursor.execute(insertSql, param)
        self.conn.commit()

        return item

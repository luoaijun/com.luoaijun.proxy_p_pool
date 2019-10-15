# coding:utf-8
import time

import scrapy
from proxySpider_scrapy.db.db_helper import DB_Helper
from proxySpider_scrapy.detect.detect_proxy import Detect_Proxy
from proxySpider_scrapy.detect.detect_manager import Detect_Manager
from proxySpider_scrapy.items import MysqlItem
from proxySpider_scrapy.utils.Utils import utils

'''
这个类的作用是将代理数据进行爬取
'''


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    start_urls = ["http://www.xicidaili.com/nn/"]
    allowed_domains = []
    db_helper = DB_Helper()
    Page_Start = 1
    Page_End = 2
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer': 'http://www.xicidaili.com/'
    }

    def parse(self, response):
        '''
        解析出其中的ip和端口
        :param response:
        :return:
        '''

        trs = response.xpath('//tr[@class="odd" or @class=""]')
        for tr in trs:
            item = MysqlItem()
            tds = tr.xpath('./td/text()').extract()
            item = MysqlItem()
            tds = tr.xpath('./td/text()').extract()
            if len(tds) < 12:
                continue
            item["ip"] = tds[0]
            item["port"] = tds[1]
            item["anonymity"] = tds[4]
            item["type"] = tds[5]
            item["alive_time"] = utils().timeTrans(tds[10])
            if tds[11] != None:
                item["final_verification_time"] = tds[11]
            item["warehousing_time"] = time.time()

            yield item
        if self.Page_Start < self.Page_End:
            new_url = self.start_urls[0] + str(self.Page_Start)
            self.Page_Start += 1
            yield scrapy.Request(new_url, headers=self.headers, callback=self.parse)

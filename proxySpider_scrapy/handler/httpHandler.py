# -*- coding: utf-8 -*-
import json

import tornado.ioloop
import tornado.web

from proxySpider_scrapy.utils.MysqlUtils import MySQLUtils

mysql = MySQLUtils("ip_pool")


class getAllHandler(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        sql = "select ip,port from ip_pool.alive_ip"
        list = []
        mysql.connect()
        mysql.cursor.execute(sql)
        size = self.get_argument('size')
        data = mysql.cursor.fetchmany(int(size))
        for i in range(0, int(size)):
            print(i)
            jsonStr = {"ip": data[i][0], "port": data[i][1]}
            list.append(jsonStr)
        self.write(json.dumps(list))


application = tornado.web.Application([(r"/getBySize", getAllHandler)])


def run():
    application.listen(10086)
    tornado.ioloop.IOLoop.instance().start()

# -*- coding: utf-8 -*-
import json

import tornado.ioloop
import tornado.web

from proxySpider_scrapy.utils.MysqlUtils import MySQLUtils

mysql = MySQLUtils("ip_pool")


class getAllHandler(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        size = self.get_argument('size')
        type = self.get_argument('type')
        sql = "select ip,port from ip_pool.alive_ip where type = " + "\"" + type + "\" " + " limit " + size
        list = []
        mysql.connect()
        mysql.cursor.execute(sql)

        data = mysql.cursor.fetchall()
        for i in range(0, len(data)):
            jsonStr = {"ip": data[i][0], "port": data[i][1]}
            list.append(jsonStr)
        self.write(json.dumps(list))


class getUrl(tornado.web.RequestHandler):

    def get(self):
        """get请求"""
        size = self.get_argument('size')
        type = self.get_argument('type')
        sql = "select url from ip_pool.alive_ip where type = " + "\"" + type + "\""
        list = []
        mysql.connect()
        mysql.cursor.execute(sql)
        data = mysql.cursor.fetchmany(int(size))
        for i in range(0, int(size)):
            print(i)
            jsonStr = {"url": data[i][0]}
            list.append(jsonStr)
        self.write(json.dumps(list))


class test(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world，test success！")
        print("success")


application = tornado.web.Application([(r"/getBySize", getAllHandler),
                                       (r"/test", test),
                                       (r"/getUrl", getUrl)])


def run():
    application.listen(10086)
    tornado.ioloop.IOLoop.instance().start()

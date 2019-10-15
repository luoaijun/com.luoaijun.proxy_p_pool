# -*- coding: utf-8 -*-

import pymysql
from scrapy.utils.project import get_project_settings


class MySQLUtils:
    def __init__(self, db_name):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PWD']
        self.name = db_name
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.name)
        self.cursor = self.conn.cursor()

    def close_spider(self):
        self.conn.close()
        self.cursor.close()

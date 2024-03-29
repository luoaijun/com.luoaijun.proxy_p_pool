#coding:utf-8
from pymongo import MongoClient

'''

数据库操作类
'''
class DB_Helper(object):


    def __init__(self):
        '''
        构造器中初始化数据库的连接
        :return:
        '''
        #连接mongo数据库,并把数据存储
        client = MongoClient("39.106.53.34",27017)#'mongodb://localhost:27017/'///'localhost', 27017///'mongodb://tanteng:123456@localhost:27017/'
        db = client.proxy
        self.proxys = db.proxys


    def insert(self,condition,value):

        '''

    :param condition: 查找条件
    :param value:  将代理信息插入数据库
    :return:
    '''
        if self.find(condition)== False:
            self.proxys.insert(value)
            return True
        else:
            return False

    def find(self,condition):
        '''

        :param condition: 查找条件
        :return:
        '''
        result = self.proxys.find_one(condition)
        if result!=None:
            return True
        else:
            return False


    def delete(self,condition):
        '''
        删除指定的数据
        :param condition: 删除条件
        :return:
        '''
        self.proxys.remove(condition)

    def updateID(self):
        proxys = self.proxys.find()
        proxyId = 1
        for proxy in proxys:
            ip = proxy['ip']
            port = proxy['port']
            self.proxys.update({'ip':ip,'port':port},{'$set':{'proxyId':proxyId}})
            proxyId +=1

#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"


from mysql_pool import Mysql

if __name__ == '__main__':
    ''
    data = ('/favicon.ico', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.4.1.14855', 200, '192.168.1.224', 'allcmd.com', '192.168.1.1', '2017-04-14 09:13:29')
    sql = "insert into nginx201705 (url,agent,status,host,http_host,clientip,accesstime) values(%s,%s,%s,%s,%s,%s,%s)"
    datas = []
    mysql=Mysql()
    while datas.__len__() < 100 :
        datas.append(data)

    for i in  range(10):
        mysql.insertMany(sql,datas)
    mysql.dispose()

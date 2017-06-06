#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

# coding:utf-8
'''
Created on 2016年5月7日
dbapi ：数据库接口
mincached ：启动时开启的空连接数量
maxcached ：连接池最大可用连接数量
maxshared ：连接池最大可共享连接数量
maxconnections ：最大允许连接数量
blocking ：达到最大数量时是否阻塞
maxusage ：单个连接最大复用次数 根据自己的需要合理配置上述的资源参数，以满足自己的实际需要。
@author: baocheng
'''
DBHOST = "192.168.1.202"
DBPORT = 3306
DBUSER = "nginx"
DBPWD = "mmmmmm"
DBNAME = "nginx_log"
DBCHAR = "utf8"
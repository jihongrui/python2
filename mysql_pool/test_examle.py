#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

# coding:utf-8
'''

@author: baocheng
'''
from mysql_pool import Mysql
from _sqlite3 import Row
from collections import Counter

clientip= []

# 申请资源
mysql = Mysql()
# kk = ('/post/id/196', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.4.1.14855', 200, '192.168.1.224', 'allcmd.com', '192.168.1.1', '2017-04-14 08:15:17')
# sql = 'insert into nginx_224 (url,agent,status,host,http_host,clientip,accesstime) values("%s","%s","%s","%s","%s","%s","%s")'
# sql = '''insert into nginx_224 (url,agent,status,host,http_host,clientip,accesstime) values(%s,%s,%s,%s,%s,%s,%s)'''
# sql = 'insert into nginx_224 (url,agent,status,host,http_host,clientip,accesstime) values '
# mysql.insertOne(sql,kk)

# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getAll(sqlAll)
# if result:
#     print "get all"
#     for row in result:
#         print "%s\t%s" % (row["uid"], row["goodsname"])
# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getMany(sqlAll, 2)
# if result:
#     print "get many"
#     for row in result:
#         print "%s\t%s" % (row["uid"], row["goodsname"])
#
# result = mysql.getOne(sqlAll)
# print "get one"
# print "%s\t%s" % (result["uid"], result["goodsname"])

result = mysql.getAll("select clientip from nginx_224 where ( agent='nws' and status=444)")
for i in result:
    clientip.append(i['clientip'])
clientip = Counter(clientip)
# most = clientip.most_common(100)
# print most
#[('111.73.157.77', 26650), ('117.145.182.17', 14336), ('111.40.174.40', 14219), ('111.40.174.44', 14195), ('111.40.174.41', 14133), ('111.40.174.42', 14127), ('111.40.174.43', 14127), ('111.202.99.165', 14112), ('106.117.249.165', 14073), ('183.203.24.11', 14068), ('112.80.27.21', 14044), ('110.53.180.30', 14026), ('120.221.31.35', 14026), ('36.49.31.19', 14025), ('183.61.13.161', 14024), ('150.138.184.35', 14024), ('103.240.126.8', 14022), ('103.240.126.7', 14008), ('1.198.4.11', 13993), ('113.105.155.141', 13993), ('103.240.126.2', 13989), ('103.240.126.4', 13988), ('103.240.126.3', 13987), ('112.5.250.152', 13980), ('112.29.196.189', 13973), ('113.200.98.151', 13971), ('117.169.98.227', 13966), ('103.240.126.5', 13953), ('180.101.217.151', 13950), ('180.153.100.141', 13949), ('120.221.31.43', 13949), ('113.105.155.26', 13944), ('180.101.217.142', 13939), ('117.131.201.20', 13936), ('117.169.98.229', 13934), ('120.221.31.12', 13934), ('117.169.98.226', 13932), ('27.221.28.141', 13932), ('218.205.82.5', 13929), ('112.5.250.148', 13928), ('1.82.242.11', 13927), ('111.26.224.100', 13924), ('180.153.100.168', 13923), ('120.221.31.11', 13922), ('111.6.160.35', 13919), ('117.131.201.21', 13916), ('150.138.222.20', 13915), ('223.111.153.11', 13914), ('42.236.126.142', 13912), ('112.5.250.145', 13911), ('223.111.153.14', 13910), ('113.207.48.143', 13910), ('180.101.217.173', 13907), ('223.111.153.43', 13905), ('103.18.208.165', 13905), ('42.236.125.24', 13905), ('112.29.199.159', 13904), ('27.221.28.153', 13902), ('117.169.71.165', 13902), ('103.18.208.141', 13902), ('218.205.82.6', 13901), ('103.18.208.171', 13900), ('42.56.76.11', 13899), ('1.199.93.31', 13899), ('182.247.250.142', 13898), ('139.215.203.142', 13898), ('223.111.153.44', 13898), ('113.107.216.35', 13897), ('103.18.208.144', 13897), ('42.236.126.141', 13897), ('117.131.201.51', 13896), ('218.205.82.8', 13895), ('183.203.65.30', 13894), ('180.101.217.31', 13892), ('223.87.3.33', 13892), ('112.5.250.139', 13891), ('117.169.71.140', 13891), ('182.247.250.174', 13891), ('183.61.13.162', 13890), ('112.5.250.142', 13890), ('42.236.125.11', 13890), ('223.87.3.28', 13890), ('117.169.98.228', 13889), ('42.56.76.44', 13889), ('223.111.153.36', 13888), ('221.180.147.36', 13888), ('180.101.217.11', 13888), ('180.101.217.43', 13887), ('150.138.184.11', 13887), ('36.101.205.14', 13885), ('183.61.13.141', 13885), ('111.161.109.104', 13885), ('223.87.3.18', 13884), ('27.152.185.165', 13884), ('223.111.153.12', 13883), ('106.119.182.44', 13883), ('42.236.125.21', 13883), ('139.215.203.151', 13883), ('150.138.176.152', 13882), ('180.101.217.12', 13882)]
#
# for u in clientip:
#     if u[-1] > 1000:


# 释放资源
mysql.dispose()
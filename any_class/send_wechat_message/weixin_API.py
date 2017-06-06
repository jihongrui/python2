#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"


import urllib
import urllib2

def do_push(message,appid=6):
    ''''''
    test_data = {'appid':appid,'message':message}
    test_data_urlencode = urllib.urlencode(test_data)
    try:
        requrl = "http://python.txkm.com/weixin/"
        req = urllib2.Request(url = requrl,data =test_data_urlencode)
        res_data = urllib2.urlopen(req)
    except:
        print("Message send is not ok")
        exit(11)

if __name__=="__main__":
    """"""
    MESS = '''
    <<苏州齐顺信息科技股份有限公司>>

报警问题:Web(pay.tianxiafu.cn)（施洪18657173553）
报警主机:192.168.88.202
报警时间:16:44:58
报警状态:PROBLEM
报警级别:High

<<苏州齐顺zabbix微信报警>>
'''
    do_push(MESS)


















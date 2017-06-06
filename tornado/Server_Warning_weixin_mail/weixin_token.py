#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

'''
每7000秒GET一次token,存入数据库 ,不好用
'''

import MySQLdb
import json
import urllib2
import time
from config import *
from log import log_file
from jsqix_mail import send_mail




def mysqldb(token):

    try:
        conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,port=MYSQL_PORT,charset="utf8")
        cur=conn.cursor()
        conn.select_db(MYSQL_DB)
        SQL = "UPDATE gettoken SET token='%s' WHERE id=1" % token
        cur.execute(SQL )
        #results = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return True

    except MySQLdb.Error,e:
        log_file("微信token更新失败")
        send_mail("微信token更新失败")
        return False
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_token():
    ''''''
    appid = "wxdda3f72fe2cb42d5"
    secrect = "N26FX62Ej5iFIPHX3cy341B8KNtji41yvNttQX62vw5gKmpbUkap4_6CczzI2d7o"
    GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (appid,secrect)
    try:
        f = urllib2.urlopen(GURL).read()
        j = json.loads(f)
        token = j['access_token']#.encode('utf8')

        if mysqldb(token):
            log_file(token)
            return token
        else:
            return False
    except:
        log_file("微信token获取失败")
        send_mail("微信token获取失败")
        print "ERROR from class get token"
        exit("error token")


if __name__ == "__main__":
    '''
    (u'Xvi8qwLxM1fqFmJTMUBOO1TcdeqUNPwegvQkSxM98iVy7IVvfJe4fsADkBoz3SVt', u'1471854446')
    '''
    while True:
        if mysqldb():
            time.sleep(7000)
        else:
            break


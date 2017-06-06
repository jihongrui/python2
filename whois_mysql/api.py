#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

import os
import time
import re
import urllib2
import MySQLdb

from log_config import debug as log_file
from weixin import do_push
from jsqix_mail import send_mail
from config import *


#取当前时间为最后检查时间
last_chkeck = time.strftime("%Y-%m-%d", time.localtime())

def get_web_url_gqsj(url,two=True):
    '''
传入域名，返回过期时间戳：1482163200
    '''
    try:
        if two == True:
            URL = 'http://whois.chinaz.com/%s' % url.decode("UTF-8").encode("GBK")
        else:
            URL = 'http://whois.chinaz.com/?Domain=%s&isforceupdate=1&ws=' % url.decode("UTF-8").encode("GBK")
        request = urllib2.Request(URL)
        link = urllib2.urlopen(request)
        page = link.read()

        re_com = re.compile(r'20[1|2]\d年[0|1]\d月\d{2}日')
        re_find = re_com.findall(page)
        re_find.sort()
        url_gqsj = re_find[-1]
        timeArray = time.strptime(url_gqsj,"%Y年%m月%d日")
        timeStamp = time.strftime("%Y-%m-%d",timeArray)
        return timeStamp
    except urllib2.HTTPError,e:
        print e
    except urllib2.URLError,e:
        print e
    except:
        print "ERROR from class <WebUrl> function <get_web_url_gqsj>"






if __name__ == "__main__" :
    ''''''
    # url = 'xuyunfei.com'
    # t = get_web_url_gqsj(url,two=False)
    # print t



#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

from mysql_pool import Mysql






if __name__ == '__main__':
    ""
    # mysql = Mysql()
    # print mysql.getOne("show status like 'uptime'")
    # mysql.dispose()
    SerIP = '192.168.85.1'
    Check_IP = int(str(SerIP).split('.')[2])
    if Check_IP in (85,101):
        SerGroup = 'hzb8'
    elif Check_IP in (88,):
        SerGroup = 'hzb9'
    elif Check_IP in (168,80):
        SerGroup = 'hzd3'
    elif Check_IP in (1,40):
        SerGroup = 'szqs'
    else:
        SerGroup = 'no'
    print SerGroup
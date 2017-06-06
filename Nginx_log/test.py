#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"
from mysql_pool import Mysql
import datetime,time,os
from jsqix_mail import send_mail

if __name__ == '__main__':
    ""
#     create_tab_sql = '''CREATE TABLE   nginx201705   (
#     log_id   bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#     url   varchar(255) NOT NULL,
#     agent   varchar(255) NOT NULL,
#     status   smallint(255) unsigned NOT NULL,
#     host   varchar(255) NOT NULL,
#     http_host   varchar(255) NOT NULL,
#     clientip   varchar(255) NOT NULL,
#     accesstime   varchar(255) NOT NULL,
#   PRIMARY KEY (  log_id  ),
#   KEY   accesstime   (  accesstime  ) USING BTREE,
#   KEY   status   (  status  ) USING BTREE
# )'''
#     mysql = Mysql()
#     print mysql.getOne("select version()")
#     mysql.getOne(create_tab_sql)
#     mysql.dispose()
    day = str(datetime.date.fromtimestamp(time.time()) + datetime.timedelta(-1))
    file_path = 'log'
    file_name = '{0}-report.txt'.format(day)
    file = os.path.join(file_path,file_name)
    msg = ''
    with open(file) as f:
        for line in f.readlines():
            msg = msg + line
    if send_mail(msg):
        print('ok')
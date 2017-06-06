#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@hotmail.com"
'''
{u'status': u'200', " \
"u'domain': u'nginx.org', " \
"u'url': u'/index.html', " \
"u'agent': u'ApacheBench/2.3'," \
" u'host': u'127.0.0.1', " \
"u'http_host': u'localhost'," \
" u'clientip': u'127.0.0.1'}


nginx config

log_format json
                 '"host":"$server_addr",'
                 '"clientip":"$remote_addr",'
                 '"http_host":"$host",'
                 '"url":"$uri",'
                 '"agent":"$http_user_agent",'
                 '"xff":"$http_x_forwarded_for",'
                 '"status":"$status",';

access_log syslog:server=192.168.1.6:20514,facility=local7,tag=nginx,severity=info json;
'''

import time
import socket, traceback
from mysql_pool import Mysql


if __name__ == '__main__':
    ''
    mysql = Mysql()
    host = ''
    port = 20514
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    Lists = list()

    while True:
        # try:

            message, address = s.recvfrom(8192)
            strs = '{' + message.split('nginx:')[-1] + '}'
            strs = eval(strs)
            List = (strs['url'], strs['agent'], int(strs['status']), strs['host'], strs['http_host'], strs['clientip'],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # print List
            Lists.append(List)
            sql = "insert into nginx201705 (url,agent,status,host,http_host,clientip,accesstime) values(%s,%s,%s,%s,%s,%s,%s)"
            # sql = 'insert into log (url,agent,status,host,http_host,clientip,accesstime) values("%s","%s","%s","%s","%s","%s","%s")'%(List)
            if len(Lists) > 10:
                nu = mysql.insertMany(sql,Lists)
                print Lists
                print "58 %s"%nu
                Lists = []
                print Lists
            #
            # mysql.insertOne(sql,List)
            s.sendto(message, address)
        # except (KeyboardInterrupt, SystemExit):
        #     raise
        # except:
        #     traceback.print_exc()
    mysql.dispose()






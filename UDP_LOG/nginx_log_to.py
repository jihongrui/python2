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
import MySQLdb

DBHOST = "192.168.1.204"
DBPORT = 3306
DBUSER = "nginx"
DBPWD = "mmmmmm"
DBNAME = "nginx_log"
DBCHAR = "utf8"

def mysql(sql,data=None):
    ""
    try:
        conn = MySQLdb.connect(host=DBHOST,port=DBPORT,user=DBUSER,passwd=DBPWD,charset=DBCHAR)
        cur = conn.cursor()
        conn.select_db(DBNAME)
        if data:
            cur.executemany(sql,data)
        else:
            cur.execute(sql)
        
    except MySQLdb.Error as e:
        print(e)
    except MySQLdb.DatabaseError as e:
        print(e)
    except MySQLdb.DataError as e:
        print(e)
    except MySQLdb.ProgrammingError as e:
        print(e)
    finally:
        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    ''
    Lists = list()

    host = ''
    port = 20514
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    while True:
        year = time.strftime("%Y", time.localtime(time.time()))
        mon = time.strftime("%m", time.localtime(time.time()))
        day = time.strftime("%d", time.localtime(time.time()))
        table = "log{}{}".format(year,int(mon))

        if int(day) == 27:
            if int(mon) != 12:
                next_mon = int(mon) + 1
                next_year = year
            else:
                next_year = int(year) + 1
                next_mon = 1
            table = "log{}{}".format(next_year, next_mon)

            create_tab_sql = '''CREATE TABLE IF NOT EXISTS {}  (
            log_id   bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            url   varchar(255) NOT NULL,
            agent   varchar(255) NOT NULL,
            status   smallint(255) unsigned NOT NULL,
            host   varchar(255) NOT NULL,
            http_host   varchar(255) NOT NULL,
            clientip   varchar(255) NOT NULL,
            accesstime   varchar(255) NOT NULL,
          PRIMARY KEY (  log_id  ),
          KEY   accesstime   (  accesstime  ) USING BTREE,
          KEY   status   (  status  ) USING BTREE
        )'''.format(table)
            mysql(create_tab_sql)

        try:
            message, address = s.recvfrom(8192)
            strs = '{' + message.split('nginx:')[-1] + '}'
            strs = eval(strs)
            List = (strs['url'], strs['agent'], int(strs['status']), strs['host'], strs['http_host'], strs['clientip'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            Lists.append(List)
            sql = 'insert into {} (url,agent,status,host,http_host,clientip,accesstime) values(%s,%s,%s,%s,%s,%s,%s)'.format(table)

            if len(Lists) > 1000:
                mysql(sql,Lists)
                Lists = []

            # mysql(sql,List)
            s.sendto(message, address)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()










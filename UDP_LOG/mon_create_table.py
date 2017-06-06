#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

import time

import MySQLdb

DBHOST = "192.168.1.204"
DBPORT = 3306
DBUSER = "nginx"
DBPWD = "mmmmmm"
DBNAME = "nginx_log"
DBCHAR = "utf8"


def mysql(sql, data=None):
    ""
    try:
        conn = MySQLdb.connect(host=DBHOST, port=DBPORT, user=DBUSER, passwd=DBPWD, charset=DBCHAR)
        cur = conn.cursor()
        conn.select_db(DBNAME)
        if data:
            cur.executemany(sql, data)
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
    ""
    year = time.strftime("%Y", time.localtime(time.time()))
    mon = time.strftime("%m", time.localtime(time.time()))
    day = time.strftime("%d", time.localtime(time.time()))
    table = "log{}{}".format(year, int(mon))
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
#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

from api import *

if __name__ == "__main__":
    '''
DROP TABLE IF EXISTS `domain`;
CREATE TABLE `domain` (
  `domain_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `group` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `expirations` date NOT NULL,
  `last_checked` date NOT NULL,
  PRIMARY KEY (`domain_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;
    '''
    # log_file("%s \t 检查开始 \t %s \n" % ('='*10,'='*10))
    try:
        conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,port=MYSQL_PORT)
        cur=conn.cursor()

        cur.execute('create database if not exists %s' % MYSQL_DB)
        conn.select_db(MYSQL_DB)
        #cur.execute('DROP TABLE IF EXISTS domain')
        cur.execute('''
CREATE TABLE `domain` (
  `domain_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `group` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `expirations` date NOT NULL,
  `last_checked` date NOT NULL,
  PRIMARY KEY (`domain_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
                    ''')




        conn.commit()
        cur.close()
        conn.close()
        # log_file("%s \t 检查结束 \t %s \n" % ('='*10,'='*10))
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

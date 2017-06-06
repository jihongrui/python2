#!/usr/bin/python
# -*- coding: utf-8 -*-
#   jihongrui@jsqix.com

#
# import pymssql
#
# conn = pymssql.connect(host='192.168.1.8', user='sz\jsqx-test', password='jihongrui789', database='sjSQL',charset="utf8")
#
# cur = conn.cursor()
#
# cur.execute('SELECT ID FROM dbo.Dm_Mobile')
# row = cur.fetchone()
#
#
# aa = row
# print aa


# conn.close()

import sys
import pymssql
class Mssql:
    def __init__(self, config):
        self.cf = config
    def __Connect(self):
        try:
            self.conn = pymssql.connect(host=self.cf['host'],user=self.cf['user'],password=self.cf['pwd'],database=self.cf['db'])
            cur = self.conn.cursor()
        except Exception, err:
            print "Error decoding config file: %s" % str(err)
            sys.exit(1)
        return cur

    def select(self, sql):
        try:
            cur = self.__Connect()
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            self.conn.close()
            return rows
        except Exception, err:
            print "Error decoding config file: %s" % str(err)
            sys.exit(1)
    def insert(self, sql):
        try:
            cur = self.__Connect()
            cur.execute(sql)
            cur.close()
            self.conn.commit()
            self.conn.close()
        except Exception, err:
            print "Error decoding config file: %s" % str(err)
            sys.exit(1)
def main():
    config = {'host':'test_db','user':'test','pwd':'123456','db':'Testdb'}
    mssql = Mssql(config)

    #select sql
    sql = "select * from test_table"
    rows = mssql.select(sql)
    #insert sql
    sql = "insert into test_table values('1','2','3')"
    mssql.insert(sql)
if __name__ == "__main__":
    main()
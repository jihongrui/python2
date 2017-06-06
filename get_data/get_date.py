#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

import MySQLdb
import sys




'''
MYSQL Server 信息
'''
MYSQL_HOST = '192.168.1.204'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = '-Pl,0okm'
MYSQL_DB = 'pydb'

def mysqldb(data):
    "批量插入"
    try:
        conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD,db=MYSQL_DB,port=MYSQL_PORT, charset="utf8")
        cur = conn.cursor()
        # conn.select_db(MYSQL_DB)
        SQL = "insert into fx_8080 values(%s,%r,%s,%s,%s,%s)"
        # cur.execute(SQL)
        # results = cur.fetchall()
        cur.executemany(SQL,data)
        conn.commit()
        cur.close()
        conn.close()
        return True

    except MySQLdb.Error, e:
        return False
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def list_to_mysql(li):
    "将list 内的数据做类型转换后,返回tuple"
    if li[1] == 'SUCCESS':
        li[1] = 0
    else:
        li[1] = round(int(li[1]) / 1000.0,3)
    if li[4][7:] == li[-1][7:]:
        li[4] = li[4]
        li[-1] = li[4]
    else:
        li[4] = li[4]
        li[-1] = li[-1][0:3]+'0000'+li[-1][7:]

    li = tuple(li)
    return li

if __name__ == '__main__':
    "脚本后跟数据文件绝对路径"
    data_file = sys.argv[1]
    Lists = []
    Inst_list = []
    f = open(data_file)  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        List = line.split()
        Lists.append(List)
        line = f.readline()
    f.close()

    for li in Lists:
        li = list_to_mysql(li)
        print li
        Inst_list.append(li)
        # 大于100条插入一次
        if len(Inst_list) > 100:
            mysqldb(Inst_list)
            Inst_list = []
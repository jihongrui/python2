#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@allcmd.com"



import os.path
import sys
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from mysql_pool import Mysql
from Config import Allow
reload(sys)
sys.setdefaultencoding('utf8')



define("port", default=58000, help="run on the given port", type=int)


class BackupHandler(tornado.web.RequestHandler):
    '''

    def get(self):
        ''''''
        self.write("hello weixin")

    def post(self):
        ''''''
        APPID = self.get_argument('appid', 6)

        MEG = self.get_argument('message', False)

        if MEG and str(APPID):
            if DO_PUSH(MEG, APPID):
                self.write("message send is ok")
            else:
                self.write("message send not ok")
    '''

    def post(self):
        '''
        +---------------+----------------------+------+-----+---------+----------------+
| Field         | Type                 | Null | Key | Default | Extra          |
+---------------+----------------------+------+-----+---------+----------------+
| sid           | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
| serip         | int(255) unsigned    | NO   | UNI | NULL    |                |
| bakserip      | int(255) unsigned    | NO   |     | NULL    |                |
| localbakdir   | varchar(255)         | NO   |     | NULL    |                |
| sourcecodedir | varchar(255)         | NO   |     | NULL    |                |
| bakserbakdir  | varchar(255)         | NO   |     | NULL    |                |
| baktime       | int(10) unsigned     | NO   |     | NULL    |                |
| sergroup      | char(4)              | NO   |     | NULL    |                |
| bakstatus     |
+---------------+----------------------+------+-----+---------+----------------+
        '''

        if self.request.remote_ip not in Allow:

            SerIP = self.get_argument('serip')
            BakSerIP = self.get_argument('bakserip')
            LocalBakDir = self.get_argument('localbakdir')
            SourceCodeDir = self.get_argument('sourcecodedir')
            BakSerBakDir = self.get_argument('bakserbakdir')
            BakTime = self.get_argument('baktime')
            BakStatus = self.get_argument('bakstatus', 0)

            Check_IP = int(str(SerIP).split('.')[2])
            if Check_IP in (85, 101):
                SerGroup = 'hzb8'
            elif Check_IP in (88,):
                SerGroup = 'hzb9'
            elif Check_IP in (168, 80):
                SerGroup = 'hzd3'
            elif Check_IP in (1, 40):
                SerGroup = 'szqs'
            else:
                SerGroup = 'no'

            data = (SerIP,BakSerIP,LocalBakDir,SourceCodeDir,BakSerBakDir,BakTime,SerGroup,BakStatus)

            sql = """
insert into sercodebackup (serip,bakserip,localbakdir,sourcecodedir,bakserbakdir,baktime,sergroup,bakstatus)
values(inet_aton({0}), inet_aton({1}),{2},{3},{4},{5},{6},{7})""".format(data)
            print sql
            mysql.insertOne(sql)





if __name__ == "__main__":
    ""
    try:
        mysql = Mysql()
        tornado.options.parse_command_line()
        app = tornado.web.Application([
            (r"/backup/", BackupHandler),

        ])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    finally:
        mysql.dispose()
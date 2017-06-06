#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from weixin import DO_PUSH
from jsqix_mail import send_mail,ABIP

from tornado.options import define, options
define("port", default=58000, help="run on the given port", type=int)



class WeixinHandler(tornado.web.RequestHandler):
    ''''''
    def get(self):
        ''''''
        self.write("hello weixin")

    def post(self):
        ''''''
        APPID = self.get_argument('appid', 6)

        MEG = self.get_argument('message',False)

        if MEG and str(APPID) :
            if DO_PUSH(MEG,APPID):
                self.write("message send is ok")
            else:
                self.write("message send not ok")

class Mailhandler(tornado.web.RequestHandler):
    ''''''
    def get(self):
        ''''''
        self.write("hello mail")

    def post(self):
        ''''''
        MEG = self.get_argument('message',False).encode("utf-8")

        IP = self.get_argument('ip',ABIP)

        TO = self.get_argument('to','jihongrui@jsqix.com')

        if MEG :
            if send_mail(MEG,TO,IP):
                self.write("mail send is ok")
            else:
                self.write("mail send not ok")


#
# class Ssvpnhandler(tornado.web.RequestHandler):
#     ''''''
#     def get(self):
#         get = Get_vpn()
#         Sers = json.dumps(get.vpnser())
#         self.write(Sers)



if __name__ == "__main__":
    ""

    tornado.options.parse_command_line()
    app = tornado.web.Application([
    (r"/weixin/", WeixinHandler),
    (r"/mail/",Mailhandler),
        # (r"/vpn/",Ssvpnhandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
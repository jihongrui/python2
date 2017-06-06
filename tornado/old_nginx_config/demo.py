#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sys
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from log import log_file
from Nginx import Nginx

reload(sys)
sys.setdefaultencoding('utf8')

define("port", default=58000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/", testHandler),
            (r"/", NginxHandler),

        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            )
        # conn = MongoClient("192.168.1.203", 57017)
        # self.db = conn["demo"]
        tornado.web.Application.__init__(self, handlers, **settings)


class NginxHandler(tornado.web.RequestHandler):
    "tornado_nginx config reset add del"
    def get(self):
        ""
        self.render("index.html")
    def post(self):
        ""
        # user = self.get_argument('user')
        # passwd = self.get_argument('passwd')
        domain = self.get_argument('domain').strip().lower()
        ip = self.get_argument('ip','127.0.0.1:80').strip()

        act = self.get_argument('act').strip().lower()
        if self.request.remote_ip in ['192.168.1.6','192.168.1.254','127.0.0.1']:
            if act in ['add','del']:
                log_file("""
客户端：\t %s \n
客户端浏览器：\t %s \n
操作域名：\t %s \n
映射IP：\t %s \n
动作：\t %s \n
                """%(self.request.remote_ip,self.request.headers['user-agent'],domain,ip,act))
                x = Nginx(domain,ip)
                if x.check():
                    if act == 'add' :
                        port = int(ip.split(':')[-1])
                        if port < 65535 and port > 0:
                            if x.check() and x.Add():
                                log_file("状态：\t OK \n")
                                self.write("OK")
                            else:
                                log_file("状态：\t ERROR \n")
                                self.write("ERROR FROM NGINX ADD")
                        else:
                            self.write("ERROR FROM PORT >0 <65535")
                    else:
                        if x.check() and x.Del() and x.reload():
                            log_file("状态：\t OK \n")
                            self.write("OK")
                        else:
                            log_file("状态：\t ERROR \n")
                            self.write("ERROR FORM NGINX DEL")
                else:
                    self.write("ERROR FORM NGINX NOT START")
            else:
                self.write("ERROR FROM ACT")
        else:
            self.write("ERROR FROM ACT ONE")




def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

import sys
import os
import subprocess
import shlex
import shutil
from log import log_file

reload(sys)
sys.setdefaultencoding('utf8')


def return_bash(cmd):
    ""

    return_command = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    return return_command.stdout.read().strip()

def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return shlex.os.system(cmd)

def check_bash_return(code):
    if code != 0:
        return False
    else:
        return True




class Nginx():
    ""
    def __init__(self,domain,server_ip='127.0.0.1:80'):
        ""
        self.domain = domain
        self.ip = server_ip
        self.nginx_config_bak = "/etc/nginx/bak/"
        self.nginx_config_path = "/etc/nginx/conf.d/"
        self.config_name = self.nginx_config_path + self.domain + ".conf"
        self.check_config_name = os.path.isfile(self.config_name)
        self.config_file = '''
server {
listen 80;
server_name  %s;
location / {
proxy_pass http://%s;
proxy_set_header Host $host;
proxy_redirect off;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_connect_timeout 60;
proxy_read_timeout 600;
proxy_send_timeout 600;
 }
}
                ''' % (self.domain,self.ip)


    def Add(self):
        ""
        try:
            if self.check_config_name:
                shutil.move(self.config_name,self.nginx_config_bak)
            with open(self.config_name,'w') as f:
                f.write(self.config_file)
            if self.reload():
                log_file("Nginx.Nginx.Add pass")
                return True
            else:
                bash("test -f %s && sudo rm -f %s" % (self.config_name, self.config_name))
                log_file("Nginx.Nginx.Add fail")
                return False
        except :
            bash("test -f %s && sudo rm -f %s" % (self.config_name,self.config_name))
            log_file("Nginx.Nginx.Add fail")
            return False


    def Del(self):
        ""
        if self.check_config_name:
            shutil.move(self.config_name, self.nginx_config_bak)
            log_file("Nginx.Nginx.Del pass")
        return True


    def check(self):
        ""
        if int(return_bash("sudo ps -ef |grep nginx |grep -v grep |wc -l")) >= 1:
            log_file("Nginx.Nginx.check pass")
            return True
        else:
            log_file("Nginx.Nginx.check fail")
            return False
    def reload(self):
        ""
        if self.check():
            return check_bash_return(bash("sudo nginx -t &>/dev/null && sudo nginx -s reload"))







if __name__ == '__main__':
    ""
    x = Nginx('sy.txkm.com','192.168.1.226:8084')
    print x.reload()





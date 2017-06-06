#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@hotmail.com"

import os
import subprocess
import threading

from Queue_test.log import log_file


class Ping():
    ''
    def __init__(self,ips='192.168.1.', nus=1, nue=255):
        ''
        self.ips = ips
        self.nus = nus
        self.nue = nue
        self.IP_list = []
        self.IP_PASS = []
        self.IP_FAIL = []

    def range_ip(self,):
        ""
        for nu in range(self.nus, self.nue):
            ip = "%s%d" % (self.ips, nu)
            self.IP_list.append(ip)

    def ping(self,ip='127.0.0.1'):
        ''''''
        try:
            if os.name == 'nt':
                result = subprocess.call(['ping', '-n', '2', '-w', '1', ip], stdout=subprocess.PIPE)
            else:
                result = subprocess.call(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
        except:
            result = 1
        finally:
            if result == 0:
                self.IP_PASS.append(ip)
            else:
                self.IP_FAIL.append(ip)


if __name__ == "__main__":
    ''

    threads = []
    nal1 = Ping()
    nal1.range_ip()
    for ip in nal1.IP_list:
        th = threading.Thread(target=nal1.ping, args=(ip,))
        th.start()
        threads.append(th)

    # 等待线程运行完毕
    for th in threads:
        th.join()

    IP_PASS = sorted(nal1.IP_PASS,key=lambda i : int(i.split('.')[-1]))
    IP_FAIL = sorted(nal1.IP_FAIL,key=lambda i : int(i.split('.')[-1]))

    while IP_PASS:
        ip = IP_PASS.pop(0)
        log_file("%s \t PASS"%ip)

    while IP_FAIL:
        ip = IP_FAIL.pop(0)
        log_file("%s \t FAIL"%ip)
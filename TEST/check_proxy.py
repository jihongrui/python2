#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"



import urllib2
import MySQLdb
import time
import socket


socket_timeout = 30

# Check proxy
def check_proxy(protocol, pip):
    ip_check_url = 'http://www.ip138.com'
    # user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'
    try:
        proxy_handler = urllib2.ProxyHandler({protocol:pip})
        opener = urllib2.build_opener(proxy_handler)
        # opener.addheaders = [('User-agent', user_agent)] #这句加上以后无法正常检测，不知道是什么原因。
        urllib2.install_opener(opener)

        req = urllib2.Request(ip_check_url)

        conn = urllib2.urlopen(req)

        detected_pip = conn.read()

        proxy_detected = True

    except urllib2.HTTPError, e:
        print "ERROR: Code ", e.code
        return False
    except Exception, detail:
        print "ERROR: ", detail
        return False

    return proxy_detected

def main():
  socket.setdefaulttimeout(socket_timeout)




  protocol = "http"
  current_proxy = "121.40.108.76:80"
  proxy_detected = check_proxy(protocol, current_proxy)
  if proxy_detected:
    print (" WORKING: " + current_proxy)
  else:
    print " FAILED: %s " % ( current_proxy, )

if __name__ == '__main__':
  main()
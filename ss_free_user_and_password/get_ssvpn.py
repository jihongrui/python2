#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

import urllib2
from BeautifulSoup import BeautifulSoup
from weixin import do_push


class Get_vpn():
    ''
    def __init__(self,url='http://www.ishadowsocks.net'):
        ''''''

        user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        request = urllib2.Request(url)
        request.add_header("User-Agent", user_agent)
        content = urllib2.urlopen(request)
        self.soup = BeautifulSoup(content)
        self.VPN_Sers = []

    def vpnser(self):
        ''''''
        trs = self.soup.findAll('div', {"class":"col-lg-4 text-center"})
        for div in trs:
            VPN_Ser = {}
            h4s = div.findAll('h4')
            if len(h4s) == 6:
                VPN_Ser['ser_add'] = h4s[0].text.strip().split(':')[-1]
                VPN_Ser['ser_port'] = h4s[1].text.strip().split(':')[-1]
                VPN_Ser['ser_passwd'] = h4s[2].text.strip().split(':')[-1]
                self.VPN_Sers.append(VPN_Ser)
        return self.VPN_Sers

if __name__=="__main__":
    ''
    url = 'http://www.ishadowsocks.net'
    get = Get_vpn(url)
    Sers = get.vpnser()
    MSGS = []
    for msg in Sers:
        print msg
        MSG = "SS_VPN_Server: \t%s\nServer_Port: \t%s\nServer_password: \t%s\n" % (msg['ser_add'],msg['ser_port'],msg['ser_passwd'])
        MSGS.append(MSG)
    message = MSGS[0] + "\n" + MSGS[1] + "\n" + MSGS[-1]
    do_push(message)




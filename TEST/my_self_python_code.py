#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

import urllib2
import MySQLdb
import sys
import time
import threading
from BeautifulSoup import BeautifulSoup

def check_proxy(protocol, pip):
    ip_check_url = 'http://www.ip138.com'
    try:
        proxy_handler = urllib2.ProxyHandler({protocol:pip})
        opener = urllib2.build_opener(proxy_handler)
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


class Get_IP():
    '''
    '''
    def __init__(self,url):
        ''''''

        user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        request = urllib2.Request(url)
        request.add_header("User-Agent", user_agent)
        content = urllib2.urlopen(request)
        self.soup = BeautifulSoup(content)
        self.ip_list = []


    def xichi(self):
        ''''''
        trs = self.soup.find('table', {"id":"ip_list"}).findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            protocol = tds[5].text.strip()
            diqu = tds[3].text.strip()
            if check_proxy(protocol,"%s:%s"%(ip,port)):
                ip_mes = {}
                ip_mes['type'] = protocol
                ip_mes['ip'] = "%s:%s" % (ip,port)
                ip_mes['diqu'] = diqu
                self.ip_list.append(ip_mes)
        return self.ip_list



    def kuaidaili(self):
        ''''''
        trs = self.soup.find('tbody').findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            ip = tds[0].text.strip()#.encode('utf8')
            port = tds[1].text.strip()#.encode('utf8')
            protocol = tds[3].text.strip()#encode('utf8')
            diqu = tds[4].text.strip()#.encode('utf8')
            # ip_mes = "%s://%s:%s" % (protocol,ip,port)
            if check_proxy(protocol,"%s:%s"%(ip,port)):
                ip_mes = {}
                ip_mes['type'] = protocol
                ip_mes['ip'] = "%s:%s" % (ip,port)
                ip_mes['diqu'] = diqu#.decode('utf8')
                self.ip_list.append(ip_mes)
        # print self.ip_list
        return self.ip_list



def range_link(Furl,Sstr,nu):
    '''
http://www.xicidaili.com/wt/2
Furl = http://www.xicidaili.com
Sstr = wt
nu = 2
    '''
    if type(Furl) == str and type(nu) == int:
        urls = []

        if type(Sstr) == str:
            url = "%s/%s/" % (Furl,Sstr)
            for nu in range(1,nu):
                urls.append("%s%s" % (url,nu))
            return urls
        elif type(Sstr) == list or type(Sstr) == tuple:
            for x in Sstr:
                url = "%s/%s/" % (Furl,x)
                for n in range(1,nu):
                    urls.append("%s%s" % (url,n))
            return urls
        else:
            pass
    else:
        return False
        print  "Type Error From %s" % sys._getframe().f_code.co_name

def go(url,DEF):
    ''''''
    try:
        if DEF == 'xc':
            xici =  Get_IP(url)
            xici_ips = xici.xichi()
            # print xici_ips
            IPS.extend(xici_ips)
            return True
        elif DEF == 'kd':
            kd = Get_IP(url)
            kd_ips = kd.kuaidaili()
            # print kd_ips
            IPS.extend(kd_ips)
            return True
        else:
            pass
    except:
        return False


def start():


    kuaidali = 'http://www.kuaidaili.com/free'
    kuaidalilei = ['inha','intr','outha','outtr']
    KDurllist = range_link(kuaidali,kuaidalilei,5)

    xicidaili = 'http://www.xicidaili.com'
    xicilei = ['nn','nt','wn','wt']
    XCurllist = range_link(xicidaili,xicilei,5)


    thread_xc = []

    for url in XCurllist:
        th = threading.Thread(target=go, args=(url,'xc'))
        th.start()
        thread_xc.append(th)

    # 等待线程运行完毕
    for th in thread_xc:
        th.join()
    thread_kd = []

    for url in KDurllist:
        th = threading.Thread(target=go, args=(url,'kd'))
        th.start()
        thread_xc.append(th)

    # 等待线程运行完毕
    for th in thread_kd:
        th.join()



if __name__=="__main__":
    ''''''
    IPS = []
    start()
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='mmmmmm',port=3306,charset='utf8')
        cur=conn.cursor()

        conn.select_db('ipdaili')
        # cur.execute('create table test(id int,info varchar(20))')
        # cur.execute('select ip from message')
        # db_list = cur.fetchall()
        # DB_list = []
        # if db_list:
        #     for ip_s in db_list:
        #         print ip_s
                # DB_list.append(ip_s[0])
        # print DB_list
        # print IPS
        #
        # IPS = list(set(IPS).difference(set(DB_list)))

        for ip in IPS:
            print ip
            print ip['diqu'],ip['ip'],ip['type']
            cur.execute('INSERT INTO message (ip,proxy_type,diqu,last_check) VALUES ("%s","%s","%s",now())' % (ip['ip'],ip['type'],ip['diqu']))
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    #
    # x = Get_IP('http://www.kuaidaili.com/free/outtr/1')
    # print x.kuaidaili()
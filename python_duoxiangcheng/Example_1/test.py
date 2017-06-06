#!/usr/bin/env python
# -*- coding:utf-8 -*-
# jihongrui@jsqix.com

import threading
from time import ctime,sleep
import datetime




def echo(object):
    ""
    # for x in range(0,5):
    print object,ctime()
    sleep(5)

def SHS():
    ""
    quch = ['151', '150', '153', '152', '155', '157', '156', '159', '158', '134', '133', '132', '131', '130', '137', '136', '135', '178', '177', '176', '139', '138', '170', '182', '183', '180', '181', '186', '187', '184', '185', '188', '189', '147', '145']
    shs = []
    while len(quch) != 0 :
        r = quch.pop()
        for x in range(0,10):
            sj = "%s%d000" % (r,x)
            shs.append(sj)
    print len(shs)
    return shs

def start(object):
    ""
    try:
        threads = []

        print "程序开始运行%s" % datetime.datetime.now()

        for cmd in object:
          th = threading.Thread(target=echo, args=(cmd,))
          th.start()
          threads.append(th)

        # 等待线程运行完毕
        for th in threads:
          th.join()
        print len(threads)
        print "程序结束运行%s" % datetime.datetime.now()
    except:
        print "ERROR from function <start>"



if __name__ == "__main__":
    ""


    quch = ['151', '150', '153', '152', '155', '157', '156', '159', '158', '134', '133', '132', '131', '130', '137', '136', '135', '178', '177', '176', '139', '138', '170', '182', '183', '180', '181', '186', '187', '184', '185', '188', '189', '147', '145']
    max_js = "9999"
    min_js = "9990"
    for xps in quch:
        sj_list = []
        sj_min = int(xps + min_js)
        sj_max = int(xps + max_js)
        while sj_min <= sj_max :
            sj_list.append(sj_min)
            print sj_min
            sj_min = sj_min + 1
        start(sj_list)
        del sj_list









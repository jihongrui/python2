#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

import os
import time
import datetime
from mysql_pool import Mysql
from jsqix_mail import send_mail
def log_file(file,msg):
    ""
    msg = "{0}\n".format(msg)
    with open(file,'a') as f:
        f.write(msg)

if __name__ == '__main__':
    ""
    mysql = Mysql()
    year = time.strftime("%Y", time.localtime(time.time()))
    mon = time.strftime("%m", time.localtime(time.time()))
    # today = time.strftime("%d", time.localtime(time.time()))
    table = "log{0}{1}".format(year, int(mon))

    day = str(datetime.date.fromtimestamp(time.time()) + datetime.timedelta(-1))
    file_path = 'log'
    file_name = '{0}-report.txt'.format(day)
    file = os.path.join(file_path, file_name)
    log_file(file, '#' * 100)
    #day = '2017-04-21'
    log_file(file,"DATE : {0}".format(day))
    log_file(file,'#' * 50)

    get_nginx_cluster = "select host,count(log_id) as nu from {0} where accesstime like '{1}%' and host in ('192.168.85.72','192.168.85.76') group by host".format(table,day)
    nginx_cluster_result = mysql.getAll(get_nginx_cluster)
    get_host = lambda x: x['host']
    get_nu = lambda x: x['nu']
    for ob in nginx_cluster_result:
        host = get_host(ob)
        nu = get_nu(ob)
        log_file(file,"Nginx Cluster Server : {0} \t Access number : {1}".format(host, nu))
    log_file(file,'#' * 50)
    pv_ip_sql = "select http_host,count(url) as PV , count(distinct clientip) as IP from {0} where accesstime like '{1}%' and status<400 group by http_host".format(table,day)

    pv_ip_result = mysql.getAll(pv_ip_sql)

    PV = lambda x: x['PV']
    IP = lambda x: x['IP']
    domain = lambda x: x['http_host']
    clien = lambda x: x['clientip']
    access_nu = lambda x: x['nu']
    for i in pv_ip_result:
        log_file(file,"域名: {0} \t PV: {1} \t IP: {2}".format(domain(i), PV(i), IP(i)))
        Domain = domain(i)
        TOP_10 = "select clientip,count(clientip) as nu  from  {0} where http_host='{1}' and accesstime like '{2}%'   group by clientip order by nu desc limit 10".format(table,Domain, day)
        TOP_10_result = mysql.getAll(TOP_10)
        for ob in TOP_10_result:
            Clien = clien(ob)
            Number = access_nu(ob)
            log_file(file," \t \t Clien_IP: {0} \t Access_number: {1}".format(Clien, Number))
        log_file(file,'-' * 50)

    mysql.dispose()
    log_file(file,'#' * 100)
    msg = ''
    with open(file) as f:
        for line in f.readlines():
            msg = msg + line
    send_mail(msg)






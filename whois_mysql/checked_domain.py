#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"


from api import *



# 取当前日期 + 30 天
nowtime = int(time.time()) + 2592000
# WarningTime 预警时间为当前时间 + 30天
WarningTime = time.strftime("%Y-%m-%d",time.localtime(nowtime))




if __name__ == "__main__":
    ''''''
    log_file("%s \t 检查开始 \t %s \n" % ('='*10,'='*10))
    try:
        conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,port=MYSQL_PORT)
        cur=conn.cursor()
        conn.select_db(MYSQL_DB)
        #查询 小于 预警时间
        cur.execute('SELECT * FROM domain WHERE expirations<"%s"' % WarningTime )
        #取得查询结果
        results = cur.fetchall()
        for row in results:
            #循环所以结果 取得domain user expirations
            domain = row[0]
            user = row[1]
            expirations = row[2]
            #强制更新domain 的 expirations
            EX_exp = get_web_url_gqsj(domain,False)
            #再次比较
            if str(EX_exp) == str(expirations):
                log_file("域名 \t %s 将在30天内过期，请使用 \t %s 登陆续费 \n" % (domain,user))
                send_mail("域名 \t %s 将在30天内过期，请使用 \t %s 登陆续费\n" % (domain,user))
                do_push("域名 \t %s 将在30天内过期，请使用 \t %s 登陆续费 \n" % (domain,user))
            else:
                cur.execute('update domain set expirations="%s",last_checked="%s" where domain_name="%s"' % (EX_exp,last_chkeck,domain))
                log_file("域名 \t %s 已更新 \n" % domain)
                send_mail("域名 \t %s 已更新 \n" % domain)
                do_push("域名 \t %s 已更新 \n" % domain)
        conn.commit()
        cur.close()
        conn.close()
        log_file("%s \t 检查结束 \t %s \n" % ('='*10,'='*10))
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

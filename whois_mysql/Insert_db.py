#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
检查 config 文件中域名是否与MYSQL中相同，若相同更新 MYSQL ==》whois ==》domain ==> last_checked
若不同插入不同的域名
/etc/crontab
00 02 */3 * * root /scripts_path/script
00 02 * * 0 root /scripts_path/script update  #加这个是要强制更新

'''
__author__ = "jihongrui@jsqix.com"


from api import *



if __name__ == "__main__":
    ''''''
    try:
        conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,port=MYSQL_PORT)
        cur=conn.cursor()
        conn.select_db(MYSQL_DB)
        #取MysqlDB中记录的条数
        cur.execute('select domain_name from domain')
        results = cur.fetchall()


        DB_LIST = []
        for row in results:
            DB_url = row[0]
            DB_LIST.append(DB_url)

        LEN_DB_URL = len(DB_LIST)

        log_file("数据库中总记录为%d\n" % LEN_DB_URL)
        log_file("配置文件中总记录为%d\n" % LEN_ALL_URL)
        #和config url总数对比
        if  LEN_DB_URL != LEN_ALL_URL :
            #不相同
            #解包ALL_COMPANY
            log_file("<config.py>配置文件记录已变化\n")
            for COMPANY in ALL_COMPANY:
                #提取管理帐号
                group = COMPANY['group']
                #取 domain name URL
                for url in COMPANY['domain']:
                    #取出过期时间
                    expirations = get_web_url_gqsj(url)
                    if url in DB_LIST:
                        log_file("更新 \t%s \t过期时间 \t%s\n" % (url,expirations))
                            #直接更新
                        cur.execute('update domain set expirations="%s",last_checked="%s" where domain_name="%s"' % (expirations,last_chkeck,url))
                    else:
                        #没有，直接 insert 域名 管理帐号 过期时间 最后检查时间
                        value = (url,group,expirations,last_chkeck)
                        cur.execute('insert into domain values(%s,%s,%s,%s)',value)
        else:
            #相同
            #循环所有domain
            for url in DB_LIST:

                expirations = get_web_url_gqsj(url)

                log_file("更新 \t%s \t过期时间 \t%s\n" % (url,expirations))
                #直接更新
                cur.execute('update domain set expirations="%s",last_checked="%s" where domain_name="%s"' % (expirations,last_chkeck,url))

        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
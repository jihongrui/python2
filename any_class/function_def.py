#!/usr/bin/env python
# -*- coding:utf-8 -*-
# jihongrui@jsqix.com

"""
解决UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in position 108: ordinal not in range(128
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def get_ip():
    """
    得到本机ip地址,Linux 下最好在 /etc/hosts 文件下把本机ip和hostname 做下对应
    :return:
    """
    import socket
    localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
    return localIP




class send_mail():
    """
    邮件发送，传入message ，ip
    """


    def __init__(self,message,ip=get_ip()):
        ""
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import smtplib


        self.msg = MIMEMultipart()
        self.msg['to'] = '15315731537@qq.com'
        self.msg['from'] = 'server@jsqix.com'
        self.msg['subject'] = ip
        self.txt = MIMEText(message,'plain','utf-8')
        self.msg.attach(self.txt)

        try:
            server = smtplib.SMTP()
            server.connect('smtp.jsqix.com')
            server.starttls()
            server.login('server@jsqix.com','UNGMTM+ODZCODI1QzYzMz&=')#XXX为用户名，XXXXX为密码
            server.sendmail(self.msg['from'], self.msg['to'],self.msg.as_string())
            server.quit()
            # print '发送成功'
        except Exception, e:
            print str(e)


def link_mongo(host='192.168.1.203',port=27017,db='domain',user='shop_phone',pwd='110800110400110',mode='SCRAM-SHA-1'):
        """
        返回已连接mongodb的object
        """
        from pymongo import MongoClient
        try:
            URL = "mongodb://%s:%s@%s:%d/%s?authMechanism=%s" % (user,pwd,host,port,db,mode)
            link = MongoClient(URL)
            return link
        except:
            print("ERROR from function <link_mongo>")



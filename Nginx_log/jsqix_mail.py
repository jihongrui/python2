#!/usr/bin/env python
# -*- coding:utf-8 -*-
# jihongrui@jsqix.com

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import os

def get_ip():
    """
    得到本机ip地址,Linux 下最好在 /etc/hosts 文件下把本机ip和hostname 做下对应
    :return:
    """
    import socket
    localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
    return localIP


def get_shell_ip():
    """"""
    IP = os.popen("ifconfig |grep 'Bcast'|grep -o 'addr:.* B'|cut -d: -f2|awk '{print $1}'",'r').readlines()
    return IP[0]




# class send_mail():

def send_mail(message):
    ""
    msg = MIMEMultipart()
    msg['to'] = '15315731537@qq.com'
    msg['from'] = 'server@jsqix.com'
    msg['subject'] = get_ip() if os.name == "nt" else get_shell_ip()
    txt = MIMEText(message,'plain','utf-8')
    msg.attach(txt)

    try:
        server = smtplib.SMTP()
        server.connect('smtp.jsqix.com')
        server.starttls()
        server.login('server@jsqix.com','UNGMTM+ODZCODI1QzYzMz&=')#XXX为用户名，XXXXX为密码
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        return True
    except Exception, e:
        print str(e)
        return False
    except:
        return False


if __name__ == '__main__':
    """
    shell script :
     /usr/bin/env python jsqix_mail.py "192.168.1.17" "`cat server.txt`"
    """
    # print get_ip()
    # print get_shell_ip()
    if send_mail("hello mail to you"):
        print 111


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# jihongrui@jsqix.com

import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


Appid_Group = {
    '1':'2',#zabbix 专用
    '6':'4',#服务器专用
    '7':'5',#DBA 专用
    '8':'6',#技术部专用
    '9':'7',#客服部专用
    '10':'8',#杭州组专用
    '11':'9' #测试专用
}




class do_push:
    """"""
    def __init__(self,message,AppID=6):
        self.appid = "wxdda3f72fe2cb42d5"
        self.secrect = "N26FX62Ej5iFIPHX3cy341B8KNtji41yvNttQX62vw5gKmpbUkap4_6CczzI2d7o"
        self.GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + self.appid + "&corpsecret=" + self.secrect
        self.App_ID = str(AppID)
        self.Group_ID = Appid_Group[self.App_ID]
        self.User_ID = '@all'
        self.Message = str(message)

        #get token
        try:
            f = urllib2.urlopen(self.GURL).read()
            j = json.loads(f)
            self.token = j['access_token']
        except:
            print "ERROR from class get token"
            exit("error token")

    # def run(self):
    #     """"""
        #set format
        self.dict_arr = {
                    "touser":self.User_ID,  #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
                    "toparty":self.Group_ID,  #企业号中的部门id
                    "msgtype":"text",
                    "agentid":self.App_ID,   #企业号中的应用id，消息类型。
                    "text":{
                        "content":self.Message
                        },
                    "safe":"0"
                    }

        try:
            self.json_template = json.dumps(self.dict_arr, ensure_ascii=False)
            self.requst_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
            self.Format_MSG = urllib2.urlopen(self.requst_url,self.json_template)
            self.return_MSG = self.Format_MSG.read()
            #读取json数据
            self.j = json.loads(self.return_MSG)
            self.j.keys()
            self.errcode = self.j['errcode']
            self.errmsg = self.j['errmsg']
            if self.errcode != 0 or self.errmsg != 'ok':
                print("wechat message sending fail\n\tERROR CODE = \t%d \t\t ERROR MESSAGE = \t %s\n" % (self.errcode,self.errmsg))
        except urllib2.HTTPError,e:
            print e
        except urllib2.URLError,e:
            print e
        except:
            print "ERROR from send message"


if __name__=="__main__":
    """"""
    # NU = 6
    # url = "http://abs.jsqix.com"
    # import time
    # App_IP = 6
    # MSG = "%s\n第 %d 次检测。\n网址：\n\t%s 已不能正常访问！！！\n" % (time.strftime("%Y-%m-%d_%H:%M:%S ", time.localtime()),NU,url)

    MSG = "苏州齐顺公司的jsqishun.com域名将在47天内过期，请用3033867178@qq.com帐号登陆续费"


    do_push(MSG)

















#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"

#################################################################

MYSQL_HOST = '192.168.80.82'
MYSQL_PORT = 3306
MYSQL_USER = 'szqsadmin'
MYSQL_PASSWD = 'mmmmmm'
MYSQL_DB = 'whois'


#################################################################
JYT_DOMAIN = [
'jingyt.cn'
]

JYT_USER = '13067706237@163.com'

JYT = {
    'group' : JYT_USER ,
    'domain' : JYT_DOMAIN
}

#################################################################

FXK_DOMAIN = [
'fanxingka.com'
]

FXK_USER = 'fanxingka@163.com'

FXK = {
    'group' : FXK_USER ,
    'domain' : FXK_DOMAIN
}

#################################################################

SZQS_DOMAIN = [
'chinayyj.cn'
,'jzgxt.net'
,'qishunsz.com'
,'szqishun.cn'
,'5917mall.cn'
,'1688buy.cn'
,'917tao.cn'
,'jsqishun.com'
,'tianxiafu.cn'
,'zhaoka.com'
]

SZQS_USER = '3033867178@qq.com'

SZQS = {
    'group' : SZQS_USER ,
    'domain' : SZQS_DOMAIN
}

#################################################################

JSQX_DOMAIN = [
    'dextx.com',
    # '德行天下.com',
    '97ma.com',
    'kswmei.com',
    'wjkaka.com',
    'qixyy.com',
    'jsqix.com',
    '7maia.com'
]

JSQX_USER = '519408891@qq.com'

JSQX = {
    'group' : JSQX_USER ,
    'domain' : JSQX_DOMAIN
}

#################################################################

ZJQS_DOMAIN  = [
'qumaika.cn',
'cy3.mobi',
'561cosplay.com',
'561cosplay.cn',
'linancha.com',
'linantea.com',
'eastra-parts.com',
'hzqiyo.cn',
'hzqiyo.com',
'hzqiyo.com.cn',
'tianxiapay.com.cn',
'tianxiapay.cn',
'tianxiapay.com',
'tianxiafu.com.cn',
'baikatong.cn',
'baikatong.com',
'baikatong.com.cn',
'kahuitong.com',
'kahuitong.cn',
'kahuitong.com.cn',
'cnkkt.com',
'wykkt.com',
'16889669.com',
'16889668.com',
'qshun.cn',
'114tg.cn',
'168kkt.cn',
'168kkt.com',
'kktong.cn',
'ournb.com',
'5imotor.com',
'haolai.com.cn',
'xuyunfei.com',
'sup01.com',
'txkm.com',
'xuyunfei.cn',
'wangyingying.com',
'qshun.com',
'cy3.cn',
'16839088.com.cn',
'16839088.cn',
'16839088.com',
'1876.cn',
'xuyuntian.com',
'xuyuntian.cn'
]

ZJQS_USER = 'hi10176252@aliyun.com'

ZJQS = {
    'group' : ZJQS_USER ,
    'domain' : ZJQS_DOMAIN
}

#################################################################
ALL_URL = JYT_DOMAIN + FXK_DOMAIN + JSQX_DOMAIN + SZQS_DOMAIN + ZJQS_DOMAIN
LEN_ALL_URL = len(ALL_URL)
ALL_COMPANY = [
    JYT,
    FXK,
    JSQX,
    SZQS,
    ZJQS
    ]
#################################################################

if __name__ == "__main__":
    '''
    print JYT
    print FXK
    print JSQX
    print SZQS
    print ZJQS
{'domain': ['jingyt.cn'], 'group': '13067706237@163.com'}
{'domain': ['fanxingka.com'], 'group': 'fanxingka@163.com'}
{'domain': ['dextx.com', '97ma.com', 'kswmei.com', 'wjkaka.com', 'qixyy.com', 'jsqix.com', '7maia.com'], 'group': '519408891@qq.com'}
{'domain': ['chinayyj.cn', 'jzgxt.net', 'qishunsz.com', 'szqishun.cn', '5917mall.cn', '1688buy.cn', '917tao.cn', 'jsqishun.com', 'tianxiafu.cn', 'zhaoka.com'], 'group': '3033867178@qq.com'}
{'domain': ['qumaika.cn', 'cy3.mobi', '561cosplay.com', '561cosplay.cn', 'linancha.com', 'linantea.com', 'eastra-parts.com', 'hzqiyo.cn', 'hzqiyo.com', 'hzqiyo.com.cn', 'tianxiapay.com.cn', 'tianxiapay.cn', 'tianxiapay.com', 'tianxiafu.com.cn', 'baikatong.cn', 'baikatong.com', 'baikatong.com.cn', 'kahuitong.com', 'kahuitong.cn', 'kahuitong.com.cn', 'cnkkt.com', 'wykkt.com', '16889669.com', '16889668.com', 'qshun.cn', '114tg.cn', '168kkt.cn', '168kkt.com', 'kktong.cn', 'ournb.com', '5imotor.com', 'haolai.com.cn', 'xuyunfei.com', 'sup01.com', 'txkm.com', 'xuyunfei.cn', 'wangyingying.com', 'qshun.com', 'cy3.cn', '16839088.com.cn', '16839088.cn', '16839088.com', '1876.cn', 'xuyuntian.com', 'xuyuntian.cn'], 'group': 'hi10176252@aliyun.com'}

    '''
    print LEN_ALL_URL
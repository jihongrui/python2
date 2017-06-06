#!/usr/bin/python
# coding=gbk

##################################################
# 注意, 如果需要换行时缩进需要跟原有的代码保持统一
##################################################

MAX_CPU_USED = 70 
MAX_WA = 20

FILTERS = ['/boot', '/dev/shm']
MIN_FREE_MB  = 500
MAX_USED_PCT = 95

PROCESS = {
#  '192.168.85.51': ['java'],
  '192.168.85.52': ['java'],
  '192.168.85.53': ['java'],
  '192.168.85.101': ['httpd'],
  '192.168.85.245': ['java']
  }

SITES = {
#  '192.168.85.51': [],
  '192.168.85.52': [
       {'site':'ds & SUP', 
       'url':'http://127.0.0.1', 
       'magic':'电商与sup'}],
  '192.168.85.53': [
       {'site':'sup interface', 
       'url':'http://127.0.0.1', 
       'magic':'sup供货平台'}],
  '192.168.85.101': [
       {'site':'static server', 
       'url':'http://127.0.0.1', 
       'magic':'static server'}],
  '192.168.85.245': [
       {'site':'test server', 
       'url':'http://127.0.0.1', 
       'magic':'测试服务器'}]
  }

FILES = {
  '192.168.85.51': [],
  '192.168.85.52': [],
  '192.168.85.53': [],
  '192.168.85.101': [],
  '192.168.85.245': []
  }
  
DEFAULT_MAILS   = ['wangmiaolong@1876.cn']
DEFAULT_MOBILES = '18967543929'

MAILS = {
  '192.168.85.51': ['caopengfei@1876.cn'],
  '192.168.85.52': ['caopengfei@1876.cn'],
  '192.168.85.53': ['caopengfei@1876.cn'],
  '192.168.85.101': ['caopengfei@1876.cn'],
  '192.168.85.245': ['caopengfei@1876.cn']
  }

MOBILES = {
  '192.168.85.51': '13067706237',
  '192.168.85.52': '13067706237', 
  '192.168.85.53': '13067706237', 
  '192.168.85.101': '13067706237', 
  '192.168.85.245': '13067706237'
  }

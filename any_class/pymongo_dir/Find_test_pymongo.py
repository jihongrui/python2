#!/usr/bin/env python
# -*- coding:utf8 -*-
# jihongrui@jsqix.com

from pymongo import MongoClient
from Link_mongo import link

URL = link('dbserver.cy3.cn',57017,'server','super_administrator','gab110xqgabjb110','sdafasdfasdf')
link = MongoClient(URL)
DB = link.server

tab = DB.free_ss_server

DB_Find = tab.find(
        {'_id':'servera'},
        {'_id':0,'addr':1,'prot':1,'password':1}
)



for Test in DB_Find:
     print Test['password']
     print Test['addr']
     print Test['prot']


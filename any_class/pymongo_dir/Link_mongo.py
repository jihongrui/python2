#!/usr/bin/env python
# jihongrui@jsqix.com

from pymongo import MongoClient


def link(host,port,database,user,password,mode):
    " function : host port database user password "
    modes = ('SCRAM-SHA-1','MONGODB-CR')
    try:
        if mode not in modes:
            mode = 'SCRAM-SHA-1'
            URL = "mongodb://%s:%s@%s:%d/%s?authMechanism=%s" % (user, password, host, port, database,mode)
            return URL
    except:
        return 'Error,Please check you input data'


if __name__ == '__main__':
    url = link('192.168.1.17',27017,'shop','shop_phone','110800110400110','asdfasdf')
    link = MongoClient(url)
    print(link)
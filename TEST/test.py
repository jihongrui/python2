#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

def get_v(d):
    for k,v in d.iteritems():
        return d[k]

a = {i: i * i for i in xrange(1)}
b = []
for i in range(10):

    b.append(a)
print b
b = tuple(b)
c = lambda d:d[0]
print map(c,b)

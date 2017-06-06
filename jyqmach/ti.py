#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"


start = 0
stop = 130

jg1 = 80
jg2 = 60
jg3 = 80
jg4 = 130




for nu1 in range(start,stop):
    for nu2 in range(start,stop):
        if nu1 + nu2 == jg1:
            for nu3 in range(start,stop):
                if  nu2 + nu3 == jg3:
                    for nu4 in range(start,stop):
                        if nu1 + nu4 == jg4 and nu4 - nu3 == jg2:
                            print nu1,nu2,nu3,nu4
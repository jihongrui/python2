#!/usr/bin/env python2
# coding=utf8

# jihongrui@jsqix.com

'''
给纪雨晴出口算题
'''

import random

# 引入log_file类,将题写入文件
from loglog import log_file


class Get_ti(object):
    "本类功能:加减法随机出题"
    def __init__(self,start,stop,num):
        "start:随机数开始 / stop:随机数停止 / num:生成题的数量"

        # 变量要求 INT 型
        try:
            self.start = int(start)
            self.stop = int(stop)
            self.num = int(num)
        except:
            # 否则报错退出
            print("ERROR FROM Get_ti start/stop/num , INT type")

    @staticmethod
    def Random(start,stop):
        "静态类"
        nu1 = random.randint(start,stop)
        nu2 = random.randint(start,stop)
        nu3 = random.randint(start,stop)
        a = nu1
        b = nu2
        c = nu3

        if c%2:
            # 减法/个位a要比个位b的小/个位a和b不等于0
            if nu1 > nu2 \
                    and int(str(a)[-1]) < int(str(b)[-1]) \
                    and int(str(a)[-1]) <> 0 \
                    and int(str(b)[-1]) <> 0 :
                ti = "%d - %d = " % (a, b)
            # 加法/个位a+b大于10/个位a和b不等于0
            elif a < b  \
                    and (int(str(a)[-1]) + int(str(b)[-1])) > 10\
                    and int(str(a)[-1]) <> 0 \
                    and int(str(b)[-1]) <> 0:
                ti = "%d + %d = " % (a, b)
            else:
                ti = False
        else:
            if int(str(a)) != int(str(b)) != int(str(c)) != 0 :
                # 连加连减
                if a < b < c :
                    ti = "%d + %d + %d =" % (a,b,c)    # 连加
                elif a > b + c :
                    ti = "%d - %d - %d =" % (a,b,c)    # 连减
                elif a > b > c:
                    ti = "%d - %d + %d =" % (a,b,c)    # 减加
                elif a < b + c :
                    ti = "%d + %d - %d =" % (b,c,a)
            else:
                ti = False

        return ti

    def Start(self):
        "while "
        while self.num:
            ti = self.Random(self.start,self.stop)
            if ti:

                # print(ti)
                print("%s%d"%(ti,eval(ti[0:-3])))
                log_file(ti,'jyq','kousuan.txt')

               # log_file(ti)
                self.num -= 1


if __name__ == '__main__':
    "调Get_ti（）"
    #    从11开始，到99结束，要出多少题

    #开始
    kaishi = 11

    #结束
    jieshu = 99

    #出题的总数
    ti = 100

    Ti = Get_ti(kaishi,jieshu,ti)
    Ti.Start()

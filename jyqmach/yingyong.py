#!/usr/bin/env python
# coding=utf8

# jihongrui@jsqix.com

'''
给纪雨晴出应用题suanchulai
'''

from random import randint as sj_nu
from random import choice as sj_rm

from loglog import log_file as log

def get_ti():
    ""
    ranming = ['小明', '小红', '小月', '小刚', '小琪', '小晴', '小旭', '小文', '小瑞', '小飞', '小熊', '大伟', '胖虎', '大雄', '小夫']
    wuping = ['个苹果', '个鸭梨', '个橡皮', '本图画本', '个玩具', '个杯子', '条鱼', '朵花']

    name1 = sj_rm(ranming)
    ranming.remove(name1)
    name2 = sj_rm(ranming)
    ranming.remove(name2)
    name3 = sj_rm(ranming)
    ranming.remove(name3)
    name4 = sj_rm(ranming)
    # ranming.remove(name4)

    wp1 = sj_rm(wuping)
    wuping.remove(wp1)
    wp2 = sj_rm(wuping)
    # wuping.remove(wp2)

    # if name1 != name2 != name3 != name4 and wp1 != wp2:
    if num1 > (num2 + num3):
        TI = "%s有%d%s,%s有%d%s,送给%s%d%s,又送给%s%d%s,问%s还有多少%s ?" % \
             (name1,num1,wp1,name4,num2,wp2,name2,num2,wp1,name3,num3,wp1,name1,wp1)
    elif num1 < (num2 + num3) and num1 > num2 >num3:
        TI = "%s有%d%s,%s有%d%s,%s有%d%s,%s有%d%s,问%s和%s比%s多几%s ?" % \
             (name1,num1,wp1,name2,num2,wp1,name3,num3,wp1,name4,num1,wp2,name2,name3,name1,wp1)
    else:
        TI = "%s有%d%s,%s有%d%s,%s有%d%s,%s有%d%s,%s有%d%s,问一共有多少%s ?" % \
             (name1,num1,wp1,name2,num2,wp1,name3,num3,wp1,name4,num1,wp2,name1,num2,wp2,wp1)
    # else:
    #     TI = False
    return TI
    # else:
    #     return False







if __name__ == '__main__':
    ""

    # 出题的总数
    ti_num_start = 1

    ti_num_end = 150

    # 开始
    kaishi = 11

    # 结束
    jieshu = 99




    while ti_num_start != ti_num_end:
        num1 = sj_nu(kaishi,jieshu)
        num2 = sj_nu(kaishi,jieshu)
        num3 = sj_nu(kaishi,jieshu)

        # print len(get_ti())
        TI =  get_ti()
        if TI:
            print(TI)
            log("<%d>  %s" % (ti_num_start,TI),'jyq','yingyong.txt')
            ti_num_start += 1
# -*- coding:UTF-8 -*-
# author: tinnarey@qq.com

'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''


def saizi_sum(num):
    if num <1:
        return
    maxnum = 6

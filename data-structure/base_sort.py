# -*- coding:utf-8 -*-
import random
def dubble_sort(seq):
    #冒泡排序 dubble sort
    lengh = len(seq)
    for i in range(lengh-1):
        for j in range(lengh-1-i):
            if seq[j] >seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]

def select_sort(seq):
    #选择排序
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        seq[i] ,seq[min_idx] = seq[min_idx],seq[i]

def insert_sort(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    for i in range(1,n):
        value = seq[i]
        pos = i
        while pos>0 and value <seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos-=1
        seq[pos] = value


seq = list(range(10))
random.shuffle(seq)
sort = sorted(seq)
insert_sort(seq)
print('ff')
assert sort==seq

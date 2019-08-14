#-*- coding: utf-8 -*-

#冒泡排序

def bubule_sort(seq):
    if len(seq) ==0:
        raise Exception('no member')
    k = 0
    for i in range(len(seq)-1):
        for j in range(len(seq)-1):
            if seq[j]<=seq[j+1]:
                revalue = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = revalue
            k +=1
    print(k)
    return seq

def insert_sort(seq):
    n= len(seq)
    if n ==0:
        raise  Exception('no member')
    for i in range(1,n):
        value = seq[i]
        pos = i
        while pos >0 and value < seq[pos-1]:

            seq[pos] = seq[pos-1]
            pos -=1

        seq[pos] = value


    # for i in range(n):
    #     for j in range(i):
    #         if seq[j] < seq[i]:
    #             seq[j],seq[i] = seq[i],seq[j]
    #         k +=1
    #     # print(seq)
    # print(k)

    return seq
import random
seq = list(range(20))
random.shuffle(seq)
print(bubule_sort(seq))
print(insert_sort(seq))
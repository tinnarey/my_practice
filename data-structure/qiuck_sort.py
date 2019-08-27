# -*-coding:utf-8 -*-

def qiuck_sort(array):
    size = len(array)
    if not array or size<2:
        return array

    pivot_idx = 0 #主元
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <=pivot and pivot_idx !=i]
    great_part = [array[i] for i in range(size) if array[i] >pivot and pivot_idx !=i]
    return qiuck_sort(less_part)+[pivot]+qiuck_sort(great_part)

def quick_inplace(array,beg,end):
    if beg < end:
        pivot = partition(array,beg,end)
        print(pivot)
        quick_inplace(array,beg,pivot)
        quick_inplace(array,pivot+1,end)

def partition(array,beg,end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index +1
    right = end -1
    while True:
        while left<=right  and array[left] < pivot:
            left +=1
        while right >= left and array[right] >= pivot:
            right -=1
        if left > right:
            break
        else:
            array[left] ,array[right] = array[right],array[left]
    array[pivot_index],array[right] = array[right],array[pivot_index]
    return right


import random
seq = list(range(10))
random.shuffle(seq)
quick_inplace(seq,0,len(seq))
assert seq == sorted(seq)
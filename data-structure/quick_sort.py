#-*- encoding:utf-8 -*-

def quicksort(array):
    size = len(array)
    if not array or size <2:#空数组或者只有一个元素的数组
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx!=i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx!=i]
    return  quicksort(less_part)+[pivot]+quicksort(great_part)

def quicksort_inplace(array,beg,end):
    if beg< end:
        pivot = partition(array,beg,end)
        quicksort_inplace(array,beg,pivot)
        quicksort_inplace(array,pivot+1,end)

def partition(array,beg,end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left]<pivot:
            left +=1
        while right >= left and array[right]>=pivot:
            right -=1
        if left>right:
            break
        else:
            array[left],array[right] = array[right],array[left]

    array[pivot_index],array[right] = array[right],array[pivot_index]

    return right

def nth_element(array,beg,end,nth):#查找array 第N 大的元素
    if beg < end:
        pivot_idx = partition(array,beg,end)
        if pivot_idx == nth-1:
            return array[pivot_idx]
        elif pivot_idx >nth -1:
            return nth_element(array,beg,pivot_idx,nth)
        else:
            return nth_element(array,pivot_idx+1,end,nth)







import random
array = list(range(10))
random.shuffle(array)
print(array)
quicksort_inplace(array,0,len(array))
print(array)
assert  array ==sorted(array)

#-*-coding:utf-8 -8-

def merge_sort(seq):
    n = len(seq)
    if n <=1:
        return seq
    else:
        mid = int(n/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
    new_seq = merge_sort_list(left_half,right_half)
    print(new_seq)
    return new_seq

def merge_sort_list(left,right):
    length_left,length_right = len(left),len(right)
    a = b =0
    new_sort_seq = list()

    while a <length_left and b <length_right:
        if left[a] < right[b]:
            new_sort_seq.append(left[a])
            a +=1
        else:
            new_sort_seq.append(right[b])
            b +=1
    if a <length_left:
        new_sort_seq.extend(left[a:])
    else:
        new_sort_seq.extend(right[b:])
    return new_sort_seq
import random
seq = list(range(10))
random.shuffle(seq)
# k = merge_sort(seq)
# print(seq,k)
assert merge_sort(seq) == sorted(seq)
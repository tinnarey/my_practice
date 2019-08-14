#-*- coding:utf-8 -*-

#list 实现array

class Array(object):
    def __init__(self,size = 32):
        self._size = size
        self._items = [None]*size #定长list？
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __len__(self):
        return self._size
    def clear(self,value = None):
        for i in range(len(self)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

if __name__ == '__main__':
    size = 10
    a = Array(size)
    for i in range(size):
        a[i] = i
    print(a[8])
    print(len(a))
    a.clear()
    print(a[8])
    print(len(a))

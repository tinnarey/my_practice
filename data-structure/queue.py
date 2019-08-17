#-*-coding:utf-8 -*-
#array  实现 队列

from collections import deque
class Array(object):
    def __init__(self,size=32):
        self._size = size
        self._items = [None]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class FullError(Exception):
    pass

class ArrayQueue(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self,value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head +=1

    def pop(self):
        value = self.array[self.tail % self.head % self.maxsize]
        self.tail +=1
        return value

    def __len__(self):
        return self.head -self.tail


#使用linklist实习队列
from linklist import LinkedList
class Node(object):
    def __init__(self,value = None,next =None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value {}, next = {}>'.format(self.value,self.next)

    __repr__ = __str__

class EmptyError(Exception):
    pass

class Queue(object):
    def __init__(self,maxsize= None):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)

    def push(self,value):
        return self._item_link_list.append(value)

    def pop(self):
        if len(self) <=0:
            raise EmptyError('empty queue')
        return self._item_link_list.popleft()

#使用Python 的deque实现队列

class MyQueue:
    def __init__(self):
        self.items = deque()
    def append(self,value):
        return self.items.append(value)
    def pop(self):
        return self.items.popleft()
    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items)

    def front(self):
        return self.items[0]


def test():
    import pytest
    size = 5
    q = Queue()
    for i in range(size):
        q.push(i)
    assert len(q) ==5
    assert q.pop() ==0
    assert q.pop() ==1
    assert q.pop() ==2
    assert q.pop() ==3
    q.pop()

    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'empty queue' == str(excinfo.value)






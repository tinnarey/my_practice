#-*- coding: utf-8 -*-

from collections import deque

class Queen(object): #实现队列，先进先出
    def __init__(self):
        self._items = deque()
    def appeend(self,value):
        return self._items.append(value)
    def pop(self):
        return self._items.popleft()
    def empty(self):
        return len(self._items) == 0

class Stack(object):#栈 先进后出
    def __init__(self):
        self._items = deque()
    def push(self,value):
        return self._items.append(value)
    def pop(self):
        return self._items.pop()
    def empty(self):
        return len(self._items) ==0

class BinTreeNode(object):
    def __init__(self,data,left = None,right =None):
        self.data ,self.left, self.right = data ,left ,right

class BinTree(object):
    def __init__(self,root = None):
        self.root = root

    @classmethod  #指改类的方法为类方法，没有此参数指定的类的方法为实例方法
    def build_from(cls,node_list): #第一个参数是类
        '''

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        :return:
        '''
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node  = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get('left')
            node.right = node_dict.get('right')
        return cls(root)

    def preorder_trav(self,subtree):
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def preoder_trav_use_stack(self,substree):
        if su


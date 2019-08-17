#--* coding:utf-8 *--

class Node(object):
    __slots__ = ('value','prev','next')

    def __init__(self,value=None,prev=None, next=None):
        self.value,self.prev,self.next = value,prev,next

class CircleDoubleLinkList(object):
    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node ,node
        self.root = node
        self.lengh = 0

    def __len__(self):
        return self.lengh
    def headnode(self):
        return self.root.next
    def tailnode(self):
        return self.root.prev

    def append(self,value):
        if self.maxsize is not None and len(self) >self.maxsize:
            raise Exception('LinkList is full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.lengh += 1

    def leftappend(self,value):
        if self.maxsize is not None and len(self) >self.maxsize:
            raise Exception('LinkList is full')
        node = Node(value)
        if self.root.next is self.root:
            self.root.next = node
            self.root.prev = node
            node.next = self.root
            node.prev = self.root
        else:
            headnode = self.root.next
            self.root.next = node
            node.next = headnode
            node.prev = self.root
            headnode.prev = node
        self.lengh +=1

    def remove(self,node):
        if node is self.root:
            return
        else:
            node.prev = node.next
            node.next.prev = node.prev
        self.lengh -=1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode #??? 是否可以去掉  ----不可以！至于为什么，，不知道

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

if __name__=='__main__':
    dll = CircleDoubleLinkList()
    assert len(dll) == 0
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert list(dll) == [1,2,3]
    headnode = dll.headnode()
    assert headnode.value == 1
    for node in dll.iter_node():
        print(node.value)






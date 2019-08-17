#

from collections import OrderedDict
from functools import wraps

def fib(n):
    '''
    斐波那契数列
    '''
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def cache(func):
    store = {}

    @wraps(func)
    def _(n):
        if n in store:
            return store[n]
        else:
            value = func(n)
            store[n] = value
            return value
    return _

@cache
def f(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)

"""
问题来了，假如空间有限怎么办，我们不可能一直向缓存塞东西，当缓存达到一定个数之后，我们需要一种策略踢出一些元素，
用来给新的元素腾出空间。
一般缓存失效策略有
- LRU(Least-Recently-Used): 替换掉最近请求最少的对象，实际中使用最广。cpu缓存淘汰和虚拟内存效果好，web应用欠佳
- LFU(Least-Frequently-Used): 缓存污染问题(一个先前流行的缓存对象会在缓存中驻留很长时间)
- First in First out(FIFO)
- Random Cache: 随机选一个删除
"""

class LRUCache:
    def __init__(self,capacity=128):
        self.capacity = capacity
        # 借助 OrderedDict 我们可以快速实现一个 LRUCache，OrderedDict 内部其实也是使用循环双端链表实现的
        # OrderedDict 有两个重要的函数用来实现 LRU，一个是 move_to_end，一个是 popitem，请自己看文档
        self.od = OrderedDict()

    def get(self,key, default=None):
        val = self.od.get(key,default)
        self.od.move_to_end(key)
        return val

    def add_or_updata(self,key,value):
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)

    def __call__(self, func):
        """
         - LRU有个缺点就是，对于周期性的数据访问会导致命中率迅速下降，
         有一种优化是 LRU-K，访问了次数达到 k 次才会将数据放入缓存
        """
        def _(n):
            if n in self.od:
                return self.get(n)
            else:
                val = func(n)
                self.add_or_updata(n,val)
                return val
        return _

@LRUCache(10)
def f_use_lru(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)

def test():
    import time
    beg = time.time()
    for i in range(50):
        print(f(i))
    print(time.time()-beg)

    beg = time.time()
    for i in range(50):
        print(f_use_lru(i))
    print(time.time()-beg)

if __name__ == '__main__':
    test()



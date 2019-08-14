#--* coding:utf-8 *--
#author:tinnarey@qq.com

class Array(object):
    def __init__(self,size=32,init= None):
        self._size = size
        self._items = [init]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,value =None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    '''
    定义hash数组的槽
    '''
    def __init__(self,key,value):
        self.key =key
        self.value = value

class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None,None)#使用过被remove

    def __init__(self):
        self._table = Array(8,init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length/float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self,key):
        return abs(hash(key))%len(self._table)

    def _find_key(self,key):
        '''

        :param key: HASH 规则算出来的key
        :return: 实际上在array里面的index，即位置
        '''
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5+1 )%_len #cpython解决哈希冲突的方式
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5+1) % _len
        return None

    def _solt_can_insert(self,index):
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED

    def _find_solt_for_insert(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._solt_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not  None

    def add(self,key,value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_solt_for_insert(key)
            self._table[index] = Slot(key,value)
            self.length +=1
            if self._load_factor >=0.8:
                self._rehash()
            return True

    def _rehash(self):
        oldtable = self._table
        newsize = len(self._table)*2
        self._table = Array(newsize,HashTable.UNUSED)
        self.length = 0
        for slot in oldtable:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_solt_for_insert(slot.key)
                self._table[index] = slot
                self.length +=1

    def get(self,key,default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self,key):
        index = self._find_key(key)
        if index is None:
            raise KeyError
        value = self._table[index].value
        self.length -=1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY,HashTable.UNUSED):
                yield slot.key

def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('hehe') is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i


if __name__ == '__main__':
    print(
        'beg',
        test_hash_table(),
        'end',
    )


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self._capacity = capacity
        self._table = OrderedDict()
    
    def find(self, isbn):
        if isbn not in self._table:
            return -1
        
        price = self._table.pop(isbn)
        self._table[isbn] = price
        return price

    def insert(self, isbn, price):
        if isbn in self._table:
            price = self._table.pop(isbn)
        
        elif len(self._table) >= self._capacity:
            self._table.popitem(last = False)
        
        self._table[isbn] = price

    def remove(self, isbn):
        return self._table.pop(isbn) is not None
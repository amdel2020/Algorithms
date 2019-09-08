# LRU Cache: Design and build a "least recently used" cache, which evicts the least recently used item. The cache should map from keys to values (allowing you to insert and retrieve a value associ­ ated with a particular key) and be initialized with a max size. When it is full, it should evict the least recently used item.

import time

class Cache:
    def __init__(self, id, data):
        self.id = id
        self.data = data

class LRUCache:
    def __init__(self, size):
        self.maxsize = size
        self.currentsize = 0
        self.lru = -1
        self.cache = []
    
    def add(self, data):
        # check limit
        # if limit crossed, delete first element from self.cache
        if self.currentsize >= self.maxsize:
            self.cache = self.cache[1:]
        
        # append to the list
        self.cache.append(data)        
    
    def get_cache(self, id):
        idx = 0
        # get the element with the given id
        for i in range(len(self.cache)):
            if self.cache[i].id == id:
                idx = i
        # move this element to the last
        self.cache.append(self.cache.pop(idx))
        return self.cache[-1]
#!/usr/bin/env python3
""" LFUCache module
Create a class LFUCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent
class BaseCaching
You can overload def __init__(self): but don’t forget to 
call the parent init: super().__init__()

def put(self, key, item):
Must assign to the dictionary self.cache_data the item
value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that 
BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU 
algorithm to discard only the least recently used you must print 
DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

from collections import defaultdict
from datetime import datetime

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching and implements the LFU eviction policy.
    """

    def __init__(self):
        """ Initialize the LFUCache class with the capacity and a frequency dictionary.
        """
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """ Add an item in the cache using LFU eviction policy.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_items = [k for k, v in self.frequency.items() if v == min_freq]
            lru_key = min(
                lfu_items, key=lambda k: self.cache_data[k].timestamp)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]
            del self.frequency[lru_key]

        self.cache_data[key] = CacheItem(item, datetime.now())
        self.frequency[key] += 1

    def get(self, key):
        """ Get an item by key from the cache using LFU eviction policy.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.cache_data[key].timestamp = datetime.now()
        return self.cache_data[key].value


class CacheItem:
    """ CacheItem class to store the item and its timestamp.
    """

    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

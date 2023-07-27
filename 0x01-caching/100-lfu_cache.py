#!/usr/bin/env python3
""" LFUCache module
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
            lru_key = min(lfu_items, key=lambda k: self.cache_data[k].timestamp)
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

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

BaseCaching = __import__('base_caching').BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache defines a caching system using LFU algorithm and inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LFUCache by calling the parent class's __init__ method
        """
        super().__init__()
        self.frequencies = {}
        self.usage_count = 0

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequency used item(s)
            min_freq = min(self.frequencies.values())
            items_to_discard = [k for k, v in self.frequencies.items() if v == min_freq]

            # If there are multiple least frequency used items, use LRU to break the tie
            lru_item = min(items_to_discard, key=lambda k: self.usage_count if k in self.cache_data else float('inf'))

            # Discard the least frequently used item
            del self.cache_data[lru_item]
            del self.frequencies[lru_item]
            print("DISCARD: {}".format(lru_item))

        self.cache_data[key] = item
        self.frequencies[key] = 1
        self.usage_count += 1

    def get(self, key):
        """ Get an item by key using LFU algorithm
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequencies[key] += 1
        self.usage_count += 1
        return self.cache_data[key]

from collections import defaultdict

BaseCaching = __import__('base_caching').BaseCaching

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)
        self.recently_used = {}

    def update_recently_used(self, key):
        self.recently_used[key] = self.recently_used.get(key, 0) + 1

    def get_least_frequently_used(self):
        min_frequency = min(self.frequency.values())
        least_frequent_items = [key for key in self.frequency if self.frequency[key] == min_frequency]
        least_recently_used_item = min(least_frequent_items, key=lambda k: self.recently_used[k])
        return least_recently_used_item

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.get_least_frequently_used()
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            del self.recently_used[discard_key]
            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.update_recently_used(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.update_recently_used(key)
        return self.cache_data[key]

# Example usage
if __name__ == "__main__":
    lfu_cache = LFUCache()

    lfu_cache.put(1, 'A')
    lfu_cache.put(2, 'B')
    lfu_cache.put(3, 'C')
    lfu_cache.put(4, 'D')

    print(lfu_cache.get(1))  # Output: A
    print(lfu_cache.get(2))  # Output: B
    print(lfu_cache.get(3))  # Output: C
    print(lfu_cache.get(4))  # Output: D

    lfu_cache.put(5, 'E')    # Least frequently used item 'A' will be discarded based on LFU and LRU algorithm.
    print(lfu_cache.get(1))  # Output: None (item 'A' has been discarded)

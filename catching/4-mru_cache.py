#!/usr/bin/env python3
"""
MRUCache class that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache
        If the cache is full, discard the most recently used item
        Print the discarded item
        If the item is not in the cache, do nothing
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recently_used_key = self.access_order[-1]
                self.cache_data.pop(most_recently_used_key)
                self.access_order.pop(-1)
                print(f"DISCARD: {most_recently_used_key}")
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """
        Get an item from the cache
        If the item is not in the cache, return None
        Update the access order when item is retrieved
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
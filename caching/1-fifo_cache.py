#!/usr/bin/env python3
"""
FIFOCache class that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        If the cache is full, discard the first item
        Print the discarded item
        If the item is not in the cache, do nothing
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        If the item is not in the cache, return None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
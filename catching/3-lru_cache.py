#!/usr/bin/env python3
"""
LRUCache class that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        # Track the order of access (most recent at the end)
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache
        If the cache is full, discard the least recently used item
        Print the discarded item
        If the item is not in the cache, do nothing
        """
        if key is not None and item is not None:
            # If key already exists, remove it from access order
            if key in self.cache_data:
                self.access_order.remove(key)

            # If cache is full, remove least recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_recently_used_key = self.access_order[0]
                self.cache_data.pop(least_recently_used_key)
                self.access_order.pop(0)
                print(f"DISCARD: {least_recently_used_key}")

            # Add new item and update access order
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """
        Get an item from the cache
        If the item is not in the cache, return None
        Update the access order when item is retrieved
        """
        if key is not None and key in self.cache_data:
            # Move key to end of access order (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
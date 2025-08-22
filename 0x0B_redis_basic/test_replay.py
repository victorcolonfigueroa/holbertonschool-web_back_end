#!/usr/bin/env python3
"""
Test the replay function
"""
from exercise import Cache, replay

# Create a cache instance
cache = Cache()

# Store some data as shown in the example
print("Storing data...")
key1 = cache.store("foo")
key2 = cache.store("bar")
key3 = cache.store(42)

print(f"Generated keys: {key1}, {key2}, {key3}")
print()

# Use replay to display the history
replay(cache.store)

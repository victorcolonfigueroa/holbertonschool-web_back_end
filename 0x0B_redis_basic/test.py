#!/usr/bin/env python3
"""
Test the Cache class
"""
from exercise import Cache

# Create a cache instance
cache = Cache()

# Test storing different types of data
data = b"hello"
key = cache.store(data)
print(f"Stored bytes data with key: {key}")

data = "Redis"
key = cache.store(data)
print(f"Stored string data with key: {key}")

data = 123
key = cache.store(data)
print(f"Stored integer data with key: {key}")

data = 3.14
key = cache.store(data)
print(f"Stored float data with key: {key}")

#!/usr/bin/env python3
"""
Test the Cache class with count_calls decorator
"""
from exercise import Cache

# Create a cache instance
cache = Cache()

# Test storing data multiple times and check call count
print("Testing count_calls decorator:")
print(f"Initial call count: {cache._redis.get('Cache.store')}")

# Call store method multiple times
data1 = cache.store(b"first")
print(f"After 1st call - Count: {cache._redis.get('Cache.store').decode('utf-8') if cache._redis.get('Cache.store') else 0}")

data2 = cache.store("second")  
print(f"After 2nd call - Count: {cache._redis.get('Cache.store').decode('utf-8')}")

data3 = cache.store(123)
print(f"After 3rd call - Count: {cache._redis.get('Cache.store').decode('utf-8')}")

data4 = cache.store(3.14)
print(f"After 4th call - Count: {cache._redis.get('Cache.store').decode('utf-8')}")

print(f"\nStored keys: {data1}, {data2}, {data3}, {data4}")
print(f"Total calls to Cache.store: {cache._redis.get('Cache.store').decode('utf-8')}")

#!/usr/bin/env python3
"""
Test the Cache class with call_history decorator
"""
from exercise import Cache

# Create a cache instance
cache = Cache()

# Test storing data multiple times and check call history
print("Testing call_history decorator:")

# Call store method multiple times with different data types
data1 = cache.store(b"first")
data2 = cache.store("second")
data3 = cache.store(123)
data4 = cache.store(3.14)

print(f"Stored keys: {data1}, {data2}, {data3}, {data4}")

# Check the inputs list
inputs = cache._redis.lrange("Cache.store:inputs", 0, -1)
print(f"\nInputs history (Cache.store:inputs):")
for i, inp in enumerate(inputs):
    print(f"  {i+1}: {inp.decode('utf-8')}")

# Check the outputs list
outputs = cache._redis.lrange("Cache.store:outputs", 0, -1)
print(f"\nOutputs history (Cache.store:outputs):")
for i, out in enumerate(outputs):
    print(f"  {i+1}: {out.decode('utf-8')}")

# Check call count (from count_calls decorator)
call_count = cache._redis.get("Cache.store")
print(f"\nTotal calls to Cache.store: {call_count.decode('utf-8') if call_count else 0}")

# Verify lists have same length
print(f"\nNumber of inputs: {len(inputs)}")
print(f"Number of outputs: {len(outputs)}")
print(f"Call count: {call_count.decode('utf-8') if call_count else 0}")

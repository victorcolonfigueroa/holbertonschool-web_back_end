#!/usr/bin/env python3
"""
Comprehensive test of all functionality
"""
from exercise import Cache, replay

def main():
    # Recreate the exact example from the task
    print("=== Testing replay function ===")
    cache = Cache()
    
    # Store data exactly as in the example
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    
    # Call replay function
    replay(cache.store)
    
    print("\n=== Additional testing ===")
    
    # Store more data
    cache.store(3.14)
    cache.store(b"bytes data")
    
    print("\nAfter storing more data:")
    replay(cache.store)
    
    print("\n=== Manual verification ===")
    # Manual check of Redis data
    print("Call count:", cache._redis.get("Cache.store").decode('utf-8'))
    print("Inputs:", [inp.decode('utf-8') for inp in cache._redis.lrange("Cache.store:inputs", 0, -1)])
    print("Outputs:", [out.decode('utf-8') for out in cache._redis.lrange("Cache.store:outputs", 0, -1)])

if __name__ == "__main__":
    main()

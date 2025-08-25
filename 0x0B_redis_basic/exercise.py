#!/usr/bin/env python3
"""
Redis Basic
"""

import redis
from typing import Optional, Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Count calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """Display the call history of a function.

    Prints the number of times the method was called and each call's
    inputs and corresponding output, using Redis lists populated by
    the call_history decorator.
    """
    qualname = method.__qualname__
    input_key = qualname + ":inputs"
    output_key = qualname + ":outputs"

    # Access the Redis client from the bound method's instance
    r = method.__self__._redis

    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)

    print(f"{qualname} was called {len(inputs)} times:")
    for in_b, out_b in zip(inputs, outputs):
        in_s = in_b.decode("utf-8")
        out_s = out_b.decode("utf-8")
        print(f"{qualname}(*{in_s}) -> {out_s}")


class Cache:
    """
    Cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key: str) -> Optional[str]:
        """
        Get string data from Redis
        """
        return self.get(key, fn=lambda raw_bytes: raw_bytes.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Get int data from Redis
        """
        return self.get(key, fn=int)

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Optional[Union[str, bytes, int, float]]:
        """
        Get data from Redis
        """
        value = self._redis.get(key)
        if value is None:
            return None
        elif fn is not None:
            return fn(value)
        return value
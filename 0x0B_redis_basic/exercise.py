#!/usr/bin/env python3
"""
Cache class for Redis operations
"""
import redis
import uuid
import functools
from typing import Union, Callable


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function
    
    Args:
        method: The method to be decorated
        
    Returns:
        Callable: The wrapped method that stores call history
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores input/output history and calls the original method"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        
        # Store input arguments using rpush
        self._redis.rpush(input_key, str(args))
        
        # Execute the original method to get the output
        output = method(self, *args, **kwargs)
        
        # Store output using rpush
        self._redis.rpush(output_key, output)
        
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called
    
    Args:
        method: The method to be decorated
        
    Returns:
        Callable: The wrapped method that increments a counter
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the counter and calls the original method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular function
    
    Args:
        method: The method to display history for
    """
    # Get the Redis instance from the method's bound instance
    # The method should be bound to an instance that has _redis attribute
    redis_instance = method.__self__._redis
    
    # Generate keys for inputs and outputs
    method_name = method.__qualname__
    input_key = method_name + ":inputs"
    output_key = method_name + ":outputs"
    
    # Get call count
    call_count = redis_instance.get(method_name)
    if call_count:
        call_count = int(call_count.decode('utf-8'))
    else:
        call_count = 0
    
    print(f"{method_name} was called {call_count} times:")
    
    # Get inputs and outputs
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)
    
    # Display each call with input -> output format
    for inp, out in zip(inputs, outputs):
        input_str = inp.decode('utf-8')
        output_str = out.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    """Cache class that stores data in Redis"""
    
    def __init__(self):
        """Initialize the Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key
        
        Args:
            data: The data to store (str, bytes, int, or float)
            
        Returns:
            str: The random key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

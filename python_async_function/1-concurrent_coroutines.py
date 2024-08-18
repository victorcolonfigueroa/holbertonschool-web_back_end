from typing import List
from 1-concurrent_coroutines import wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay seconds n times,
    and returns a sorted list of the resulting delay times.
    
    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay time in seconds.
    
    Returns:
        List[float]: A sorted list of the delay times.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key
        
    return delays

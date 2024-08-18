import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    n times, and returns a sorted list of the resulting delay times.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay time.

    Returns:
        List[float]: A sorted list of the delay times.

    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key
        
    return delays

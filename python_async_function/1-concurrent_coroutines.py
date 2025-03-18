import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with specified max_delay
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay in seconds
    Returns:
        List of delays in ascending order
    """
    delays = []
    tasks = []

    for i in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
#!/usr/bin/env python3

"""this async coroutine takes an int and waits for random delay"""


import random
import asyncio


# function
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): The maximum delay. Defaults to 10.

    Returns:
        int: The actual delay used.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
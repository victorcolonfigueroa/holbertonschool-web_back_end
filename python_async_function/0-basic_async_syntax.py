#!/usr/bin/env python3

"""this async coroutine takes an int and waits for random delay"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns random delay"""
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
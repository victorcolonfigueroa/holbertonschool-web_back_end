#!/usr/bin/env python3
"""
4. Tasks
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns task_wait_random n times with specified max_delay
    Args:
        n: number of times to spawn task_wait_random
        max_delay: maximum delay in seconds
    Returns:
        List of delays in ascending order
    """
    delays = []
    tasks = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
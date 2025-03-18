#!/usr/bin/env python3
"""
3. Tasks
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asynchronous task that waits for a random
    delay between 0 and max_delay (inclusive) seconds
    and returns the actual delay used.
    """
    return asyncio.create_task(wait_random(max_delay))
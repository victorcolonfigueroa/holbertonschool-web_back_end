import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task object that wraps the wait_random function.

    Args:
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object that represents the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

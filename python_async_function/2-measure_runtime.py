
#!/usr/bin/env python3
"""
2. Measure the runtime
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of exec wait_n n times with max_delay

    Args:
        n (int): The number of times to execute wait_n
        max_delay (int): The max delay in seconds

    Returns:
        float: The average time per execution of wait_n
    """
    starting_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    ending_time = time.perf_counter()

    total_time = ending_time - starting_time
    return total_time / n

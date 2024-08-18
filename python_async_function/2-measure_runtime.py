import asyncio
import time
from 1-concurrent_corountines import wait_n


import time
import asyncio

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay for each call to the wait_n function.

    Returns:
        float: The average runtime of the wait_n function in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time -  start_time
    return total_time / n

import random
import asyncio


async def async_generator():
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This generator uses the `asyncio.sleep` function to introduce a delay of 1 second
    between each yield statement. It yields a total of 10 random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

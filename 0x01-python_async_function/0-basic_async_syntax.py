#!/usr/bin/env python3
"""
This module covers: The basics of async
"""


import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """
    This function is an asynchronous coroutine that takes in an
    integer argument (max_delay, with a default value of 10) named
    wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int): This max delay argument with a default value of 10

    Returns:
        (float): the number of seconds the function delayed before
        returning a response
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

asyncio.run(wait_random())

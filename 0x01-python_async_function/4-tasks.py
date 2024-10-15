#!/usr/bin/env python3
"""
This module covers: Let's execute multiple coroutines at the same
time with async
"""


from typing import Callable, Awaitable, List


wait_random: Callable[[int], Awaitable[float]] = \
    __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays: List = []

    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays

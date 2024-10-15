#!/usr/bin/env python3
"""
This module measures the runtime of wait_n.
"""


import time
import asyncio
from typing import Callable, Awaitable, List


wait_n: Callable[[int, int], Awaitable[List[float]]] = \
    __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time

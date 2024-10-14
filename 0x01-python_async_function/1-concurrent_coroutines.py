#!/usr/bin/env python3
"""
This module covers: Let's execute multiple coroutines at the same time with async
"""


import random
import asyncio
from typing import Callable, Awaitable, List


wait_random: Callable[[int], Awaitable[float]] = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay:int):
    delays: List = []

    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    
    return delays

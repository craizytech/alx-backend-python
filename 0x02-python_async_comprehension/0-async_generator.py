#!/usr/bin/env python3
"""
This module creates an asynchronous generator.
"""

import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[int, None]:
    """
    This coroutine loops 10 times and each time asynchronously waits
    for 1 second then yields a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

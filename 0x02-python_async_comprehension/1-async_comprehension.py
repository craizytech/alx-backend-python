#!/usr/bin/env python3
"""
This module covers the asyncronous comprehension concept
"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine iterates over a generator object asynchronously
    and adds that particular element to a list.
    """
    return [i async for i in async_generator()]

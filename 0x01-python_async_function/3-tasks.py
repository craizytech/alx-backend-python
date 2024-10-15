#!/usr/bin/env python3
"""
This module covers the asyncio task
"""


import asyncio
from asyncio import Task
from typing import Callable, Awaitable


wait_random: Callable[[int], Awaitable[float]] = \
    __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    This function uses the asyncio module to create a
    asyncio task that needs to be awaited.

    Args:
        max_delay (int): The number of seconds to delay the function

    Returns:
        Awaitable Object (Task): This is an object that needs awaiting
    """
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""
This module covers: Run time for four parallel comprehensions
"""


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function runs 4 instances of the async_comprehension in
    parallel or concurently and then measures it's total runtime and
    returns it.

    Returns:
        float: time that it takes to run the 4 processes
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        )

    end_time = time.time()

    total_time = end_time - start_time

    return total_time

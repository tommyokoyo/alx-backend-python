#!/usr/bin/env python3
"""
    Loops 10 times, each time asynchronously waiting
    1 second and yield a number between 0 and 10
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Executes async_comprehension four times in parallel using
        asyncio.gather and measure total runtime
        :Return: run time
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                           async_comprehension(), async_comprehension())
    total_runtime = time.perf_counter() - s
    return total_runtime

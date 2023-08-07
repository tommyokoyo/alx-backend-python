#!/usr/bin/env python3
"""
    Loops 10 times, each time asynchronously waiting
    1 second and yield a number between 0 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        Generate Numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

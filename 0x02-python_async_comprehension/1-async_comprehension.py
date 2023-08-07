#!/usr/bin/env python3
"""
    Loops 10 times, each time asynchronously waiting
    1 second and yield a number between 0 and 10
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        This coroutine collects 10 numbers from the async_generator
        and returns them
        :Return: 10 random numbers
    """
    return [g async for g in async_generator()]

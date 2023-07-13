#!/usr/bin/env python3
"""
    Function task_wait_random that returns an asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Function that takes a max delay value and returns
        a task
        :param max_delay: int
        :return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))

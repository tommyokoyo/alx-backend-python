#!/usr/bin/env python3
"""
    Takes 2 int args and waits for random delay
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        Waits for a random delay (max_delay - n)
        :param n:
        :param max_delay:
        :return @list: All delays in ascending order
    """
    spawn_list = []
    delay_list = []

    for i in range(n):
        new_task = asyncio.create_task(wait_random(max_delay))
        new_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(new_task)

    for spawn in spawn_list:
        await spawn

    return delay_list

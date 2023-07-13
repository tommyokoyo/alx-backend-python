#!/usr/bin/env python3
"""
    Takes code from wait_n and alter it into a new
    function task_wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Waits for a random delay (max_delay - n)
        :param n:
        :param max_delay:
        :return @list: All delays in ascending order
    """
    spawn_list = []
    delay_list = []

    for i in range(n):
        new_task = asyncio.create_task(task_wait_random(max_delay))
        new_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(new_task)

    for spawn in spawn_list:
        await spawn

    return delay_list

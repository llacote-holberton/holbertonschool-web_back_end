#!/usr/bin/env python3
"""Enhancing previous sleep example with ordered async repetition"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn sleeps n times  as tasks, return delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    chosen_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        chosen_delays.append(delay)
    return chosen_delays

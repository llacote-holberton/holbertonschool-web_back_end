#!/usr/bin/env python3
"""Enhancing previous sleep example with ordered async repetition"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    chosen_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        chosen_delays.append(delay)
    return chosen_delays

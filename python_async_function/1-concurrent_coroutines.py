#!/usr/bin/env python3
"""Enhancing previous sleep example with ordered async repetition"""

import asyncio
from typing import List

# Cannot work because of '-' character
# from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    chosen_delays = []
    for task in asyncio.as_completed(tasks):
        chosen_delays.append(await task)
    return chosen_delays

# ===== Task instructions =====
# Import wait_random from the previous python file that you've written
#   and write an async routine called wait_n that takes in 2 int arguments
#   (in this order): n and max_delay.
# You will spawn wait_random n times with the specified max_delay.
# Wait_n should return the list of all the delays (float values).
# The list of the delays should be in ascending order without using sort()
#   because of concurrency.

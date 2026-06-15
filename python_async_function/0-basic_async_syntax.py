#!/usr/bin/env python3
"""Basic module forcing script to wait random time"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronously wait up to max_delay seconds"""

    # randrange returns int and excludes upper bound
    # delay = random.randrange(0, max_delay)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# ===== Task instructions =====
# Write an asynchronous coroutine...
#  * Named wait_random
#  * That takes in an integer argument (max_delay, with a default value of 10)
#  * That waits for a random delay in seconds between 0 and max_delay included
#      (as a float value) and eventually returns it.
# Use the random module.

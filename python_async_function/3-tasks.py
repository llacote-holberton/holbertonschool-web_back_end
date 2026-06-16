#!/usr/bin/env python3
"""Enhancing previous sleep example with ordered async repetition"""

import time
import asyncio

# Cannot work because of '-' character
# from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """Returns a 'wait_random' task"""
    return asyncio.create_task(wait_random(max_delay))


# ===== Task instructions =====
# Write a function (do not create an async function,
#   use the regular function syntax to do this) task_wait_random
#   that takes an integer max_delay and returns a asyncio.Task.

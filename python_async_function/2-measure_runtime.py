#!/usr/bin/env python3
"""Enhancing previous sleep example with ordered async repetition"""

import time
import asyncio

# Cannot work because of '-' character
# from 0-basic_async_syntax import wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures average time for task completion"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n


# ===== Task instructions =====
# Create a measure_time function with integers n and max_delay as arguments
#   that measures the total execution time for wait_n(n, max_delay),
#   and returns total_time / n. Your function should return a float.
# Use the time module to measure an approximate elapsed time.

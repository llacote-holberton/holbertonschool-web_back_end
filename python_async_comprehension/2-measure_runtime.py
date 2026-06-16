#!/usr/bin/env python3
"""Module parallelizing creation of 4 lists of 10 random numbers"""
import random
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total time of running 4*10 random numbers gen in parallel"""
    start_time = time.time()
    random_lists_generators = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*random_lists_generators)
    # Reminder: gather expects n individual arguments -> need list unpacking
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))


# ===== Task instructions =====
# Import async_comprehension from the previous file and
#   write a measure_runtime coroutine that will
#   execute async_comprehension four times in parallel using asyncio.gather.
# measure_runtime should measure the total runtime and return it.
# Notice that the total runtime is roughly 10 seconds, explain it to yourself.

# === Self-Learning notes ===
# Explanation of the "notice" in instructions is simple.
# Although we spare much time by running in parallel, each execution of
#   async_comprehension will still last roughly 10 sec by design since
#   it has been written to "provide 10 numbers, one per passing second".
#
# Reminder: this hereafter...
# random_lists_generators = [async_comprehension() for _ in range(4)]
# is a condensed version of
# random_lists = []
# for _ in range(4):
#     new_list = async_comprehension()
# random_lists.append(new_list)

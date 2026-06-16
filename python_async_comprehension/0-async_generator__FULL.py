#!/usr/bin/env python3
"""Provides a basic random number generator waiting between each pick"""
import asyncio                      # Required for async processes.
from typing import AsyncGenerator   # Required for proper coroutine signature.
import random                       # Just to randomized numbers picked.


# Async def => defines a Coroutine
# "_generator" to note that we use the 'yield' mechanic instead of plain return
# Return signature has two values: first for yield, second for "bonus value"
#   when function ends.
async def async_generator() -> AsyncGenerator[float, None]:
    """Generates 10 rounds of 'sleep 1s and pick random float' instructions"""
    loop_cycles = 10
    for _ in range(loop_cycles):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number


# ===== Task instructions =====
# Write a coroutine called async_generator that takes no arguments.
# The coroutine will loop 10 times, each time asynchronously wait 1 second
#   then yield a random number between 0 and 10. Use the random module.

# ===== Self notes =======
# Any function can have both yield and return, but return has a slightly
#   different meaning.
# Pick example of a function distributing slices of a pie.
#   yield would give a slice to each user requesting,
#   when return could give the total number of slices distributed.
# TECHNICALLY the return value is wrapped inside a StopAsyncIteration exception
#   which is automatically raised when the generator has nothing left to yield
#   (inside the 'value' attribute) so we need to use try/except at caller level
# This is different from a generator interrupted with a break or something in
#   in which case Python silently calls aclose() on the generator, which
#   deletes without even raising exception, so need to use try/finally.

#!/usr/bin/env python3
"""Provides a basic random number generator waiting between each pick"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates 10 rounds of 'sleep 1s and pick random float' instructions"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

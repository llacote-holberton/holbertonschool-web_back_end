#!/usr/bin/env python3
"""Provides a basic random number generator waiting between each pick"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Generates 10 rounds of 'sleep 1s and pick random float' instructions"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

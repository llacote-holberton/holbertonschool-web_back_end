#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
print(asyncio.run(wait_n(0, 10)))   # n=0 → liste vide ?
print(asyncio.run(wait_n(1, 0)))    # n=1, max=0 → [0.0] ?
print(asyncio.run(wait_n(1, 10)))   # n=1 → [x] ?

#!/usr/bin/env python3
"""Exécution de multiples coroutines en parallèle avec asyncio"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Exécute wait_random n fois en parallèle et renvoie les délais triés"""
    # On crée une liste de coroutines simples (sans create_task)
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # asyncio.as_completed prend en charge la parallélisation et le tri naturel
    return [await task for task in asyncio.as_completed(tasks)]

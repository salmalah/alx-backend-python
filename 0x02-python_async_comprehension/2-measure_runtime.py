#!/usr/bin/env python3
"""
This module is the define the contains a coroutine called measure_runtime
"""

from typing import List
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension four times
    in parallel and measures the total runtime"""
    start_t = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_t = asyncio.get_event_loop().time()
    return end_t - start_t

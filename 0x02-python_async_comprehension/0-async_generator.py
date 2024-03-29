#!/usr/bin/env python3
"""
This module is to Write a coroutine called async_generator
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields
    random number between 0 and 10 after waiting for 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        n = random.uniform(0, 10)
        yield n

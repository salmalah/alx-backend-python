#!/usr/bin/env python3
"""
This module is the create The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

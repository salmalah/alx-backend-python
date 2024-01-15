#!/usr/bin/env python3
"""
this module isexecute multiple coroutines at the same time with async
"""
from typing import List
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    list = [await t for t in asyncio.as_completed(delays)]
    return list

#!/usr/bin/env python3
"""
This module is the create an asyncio.Task for wait_n
"""

import asyncio
from typing import List, Any

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for wait_random n times with the specified max_delay
    Returns: List[float]: List of delays (float values) in ascending order
    """
    tasks = []
    delays = []

    for i in range(n):
        ts = task_wait_random(max_delay)
        tasks.append(ts)

    for ts in asyncio.as_completed((tasks)):
        delay = await ts
        delays.append(delay)

    return delays

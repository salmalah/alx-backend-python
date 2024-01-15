#!/usr/bin/env python3
"""
using wait_random from 0-basic_async_syntax
Write function task_wait_random
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer max_delay
    return: Task object representing the execution of wait_random
    """
    return (asyncio.create_task(wait_random(max_delay)))

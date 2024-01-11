#!/usr/bin/env python3
"""
This is a module define function make_multiplier that takes
a float multiplier as argument
"""
from typing import Callable


def make_multiplier (multiplier: [[float], float]) -> Callable[[float], float]:
    """Add a float multiplier as argument and returns a
    function that multiplies a float"""
    return (multiplier**multiplier))

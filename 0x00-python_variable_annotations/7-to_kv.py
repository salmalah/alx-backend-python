#!/usr/bin/env python3
"""
This is a module function to_kv that takes a string k
and an int OR float v as arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Add int or float return Tuple"""
    return (str, (v**2))

#!/usr/bin/env python3
"""
Type annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the iterable
    Returns: List[Tuple[Sequence, int]]: A list of tuples
    """
    return [(i, len(i)) for i in lst]

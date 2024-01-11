#!/usr/bin/env python3
"""
module to Write a type-annotated function sum_list which takes a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ take list of float
    return sum"""
    return sum(input_list)

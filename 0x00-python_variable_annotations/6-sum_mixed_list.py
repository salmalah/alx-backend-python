#!/usr/bin/env python3
"""
module to define unction sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ take list of int, float
    return sum"""
    return sum(mxd_lst)

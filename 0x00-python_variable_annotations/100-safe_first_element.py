#!/usr/bin/env python3
"""
this module the correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence
    Returns: Union[Any, None]: The first element of the sequence
    """
    if lst:
        return lst[0]
    else:
        return None

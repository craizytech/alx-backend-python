#!/usr/bin/env python3
"""
This module creates a string and a tuple out of
a string and a float
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function creates a tuple out of a string and a float

    Args:
        k (str): first argument
        v (int | float): second argument

    Returns:
        (tuple) : 1st element as k and 2nd element as v
    """
    return (k, float(v ** 2))

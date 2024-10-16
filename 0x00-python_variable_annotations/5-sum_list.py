#!/usr/bin/env python3
"""
this module takes a list and returns their sum
as float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of integers and floats
    and returns their sum as float.

    Args:
        input_list (List): list of integers anf floats

    Returns:
        (float) : The sum of the contents in the list.
    """
    return sum(input_list)

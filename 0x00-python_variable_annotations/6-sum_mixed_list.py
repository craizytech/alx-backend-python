#!/usr/bin/env python3
"""
this module takes a list of ints and floats then
returns their sum as float
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats
    and returns their sum as float.

    Args:
        mxd_list (List): list of integers anf floats

    Returns:
        (float) : The sum of the contents in the list.
    """
    return float(sum(mxd_list))

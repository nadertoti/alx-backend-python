#!/usr/bin/env python3
"""
Complex function types - mixed list
Returns their sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return a sum of list of int and float
    """
    return sum(mxd_lst)

#!/usr/bin/env python3
"""
Function Complex types - functions
Returns function that multiplies a float by a multipier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a muliplier for to values
    """

    def fn(num: float):
        return num * multiplier
    return fn

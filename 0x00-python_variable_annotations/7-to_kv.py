#!/usr/bin/env python3
"""
Function Complex types - string and int/float to tuple
Returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return Tuple of int and float value
    """
    return (k, v * v)

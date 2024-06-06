#!/usr/bin/env python3
"""
Function that make iterable argu
using annotate syntax function
Return param values
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate function param
    element_length
    """
    return [(i, len(i)) for i in lst]

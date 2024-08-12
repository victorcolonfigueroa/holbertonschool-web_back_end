#!/usr/bin/env python3
from typing import List, Union
"""function that takes a list of ints, floats and returns their sum as a float"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum"""
    return sum(mxd_lst)
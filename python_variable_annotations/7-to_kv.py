#!/usr/bin/env python3
from typing import Union, Tuple


"""function args"""
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the the list"""
    return (k, float(v ** 2))

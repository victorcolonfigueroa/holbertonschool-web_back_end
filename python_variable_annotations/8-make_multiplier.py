#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given value by the
    specified multiplier.

    Args:
        multiplier (float): The multiplier to be used for multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float value
        and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function

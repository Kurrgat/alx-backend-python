#!/usr/bin/env python3
"""
takes a float multiplier as argument
and returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float argument
    and returns the multiplied result.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func

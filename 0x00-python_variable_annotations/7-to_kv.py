#!/usr/bin/env python3
"""
takes a string k and an int OR float v as arguments and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element as the string k
    and the second element
    as the square of the int/float v.

    Args:
    k (str): A string.
    v (Union[int, float]): An integer or float number.

    Returns:
    Tuple[str, float]: A tuple where the first element is k
    and the second element is v squared.
    """
    return (k, float(v ** 2))

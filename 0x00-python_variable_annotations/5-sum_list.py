#!/usr/bin/env python3
"""
takes a list input_list of floats as argument and returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of the list of float numbers.
    """
    return sum(input_list)

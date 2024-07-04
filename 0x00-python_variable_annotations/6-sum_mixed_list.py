#!/usr/bin/env python3
"""
takes a list mxd_lst of integers and floats and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and float numbers.

    Returns:
    float: The sum of the list of numbers as a float.
    """
    return sum(mxd_lst)

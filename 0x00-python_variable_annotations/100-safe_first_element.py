#!/usr/bin/env python3
"""Task 10"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Args:
    lst (Sequence[Any]): A sequence (list, tuple, etc.)
    of elements of any type.

    Returns:
    Union[Any, None]: The first element of the list if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

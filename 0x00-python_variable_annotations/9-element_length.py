#!/usr/bin/env python3
"""Task 9"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples
    where each tuple contains an element from lst and its length.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences
    (e.g., list, tuple, string).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where
    the first element is from lst and the second element is its length.
    """
    return [(i, len(i)) for i in lst]

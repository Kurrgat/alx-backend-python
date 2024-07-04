#!/usr/bin/env python3
"""Task 11"""


from typing import Mapping, Any, TypeVar, Union

# Define a type variable ~T
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with 'key' from 'dct'.
    If 'key' exists in 'dct', returns its corresponding value.
    If 'key' does not exist in 'dct', returns 'default'.

    Args:
    dct (Mapping): A mapping type (dictionary-like object).
    key (Any): The key to lookup in the dictionary.
    default (Union[T, None], optional): The default value to return
    if 'key' is not found. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with 'key'
    if found in 'dct', otherwise 'default'.
    """
    if key in dct:
        return dct[key]
    else:
        return default

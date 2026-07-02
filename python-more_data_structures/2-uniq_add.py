#!/usr/bin/python3
"""Module that adds all unique integers in a list"""


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)

    Args:
        my_list: list of integers

    Returns:
        The sum of unique integers
    """
    return sum(set(my_list))

#!/usr/bin/python3
"""Module that returns elements present in only one of two sets"""


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set

    Args:
        set_1: first set
        set_2: second set

    Returns:
        A set of elements present in only one of the two sets
    """
    return set_1 ^ set_2

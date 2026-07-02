#!/usr/bin/python3
"""Module that returns common elements between two sets"""


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Returns:
        A set of elements present in both sets
    """
    return set_1 & set_2

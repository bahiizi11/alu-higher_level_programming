#!/usr/bin/python3
"""Module that defines a function to check exact class membership"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if type(obj) is a_class, otherwise False
    """
    return type(obj) is a_class

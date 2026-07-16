#!/usr/bin/python3
"""Module that defines a function to check class or inheritance membership"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or a subclass of it

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a_class or a subclass, otherwise False
    """
    return isinstance(obj, a_class)

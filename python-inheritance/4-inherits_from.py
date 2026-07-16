#!/usr/bin/python3
"""Module that defines a function to check strict inheritance"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited from a_class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj's class inherited (directly or indirectly) from
        a_class, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Module that defines a function to look up an object's attributes"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: the object to inspect

    Returns:
        A list of attribute and method names
    """
    return dir(obj)

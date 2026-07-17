#!/usr/bin/python3
"""Module that defines a function to build a serializable dict"""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure object

    Args:
        obj: an instance of a class whose attributes are all serializable

    Returns:
        A dictionary representation of the object's attributes
    """
    return obj.__dict__

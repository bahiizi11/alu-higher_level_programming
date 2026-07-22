#!/usr/bin/python3
"""Module for adding two integers.

This module defines a single function, add_integer, that returns
the sum of two integers or floats, casting floats to integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to int.

    Raises TypeError if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""Module for printing a square made of the # character."""


def print_square(size):
    """Print a square of size `size` using the # character.

    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

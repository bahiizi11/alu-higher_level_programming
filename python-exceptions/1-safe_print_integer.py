#!/usr/bin/python3
"""Module that safely prints an integer"""


def safe_print_integer(value):
    """Prints an integer with "{:d}".format()

    Args:
        value: the value to print (any type)

    Returns:
        True if value was printed as an integer, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

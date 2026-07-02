#!/usr/bin/python3
"""Module that safely divides two integers"""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result

    Args:
        a: the numerator
        b: the denominator

    Returns:
        The value of the division, otherwise None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

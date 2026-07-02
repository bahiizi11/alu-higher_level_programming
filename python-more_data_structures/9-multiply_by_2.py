#!/usr/bin/python3
"""Module that multiplies all values of a dictionary by 2"""


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: the dictionary (all values are integers)

    Returns:
        A new dictionary with doubled values
    """
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary

#!/usr/bin/python3
"""Module that replaces or adds a key/value in a dictionary"""


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary

    Args:
        a_dictionary: the dictionary
        key: the key (always a string)
        value: the value (any type)

    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary

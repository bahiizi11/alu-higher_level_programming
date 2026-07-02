#!/usr/bin/python3
"""Module that replaces all occurrences of an element in a list"""


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list

    Args:
        my_list: the initial list
        search: the element to replace
        replace: the new element

    Returns:
        A new list with occurrences replaced
    """
    return [replace if item == search else item for item in my_list]

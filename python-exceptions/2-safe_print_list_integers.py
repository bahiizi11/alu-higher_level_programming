#!/usr/bin/python3
"""Module that safely prints and counts integers of a list"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list, only integers

    Args:
        my_list: the list to print from
        x: the number of elements to access

    Returns:
        The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count

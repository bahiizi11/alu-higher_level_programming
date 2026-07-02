#!/usr/bin/python3
"""Module that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer

    Args:
        roman_string: the Roman numeral string

    Returns:
        The integer value, or 0 if roman_string is not a valid string
    """
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

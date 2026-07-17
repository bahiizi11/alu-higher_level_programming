#!/usr/bin/python3
"""Module that defines a function to write a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8), overwriting existing content

    Args:
        filename: the path of the file to write to
        text: the string to write

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

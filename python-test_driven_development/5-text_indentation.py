#!/usr/bin/python3
"""Module for printing text with indentation after ., ? and :."""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? or : character.

    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for i, char in enumerate(text):
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")

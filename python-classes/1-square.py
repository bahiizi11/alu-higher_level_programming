#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new Square

        Args:
            size: the size of the square
        """
        self.__size = size
